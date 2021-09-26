from flask_appbuilder import BaseView, expose
from airflow.version import version
from flask import jsonify, request
from airflow import configuration
from simple_dag_editor.commons import ROUTE, MENU_CATEGORY, MENU_LABEL, JS_FILES
from simple_dag_editor.utils import Storage, TreeUtils

__all__ = ['appbuilder_view']

# AppBuilder (Airflow >= 2.0)

try:
    from airflow.www import auth
    from airflow.security import permissions

    PERMISSIONS = [
        (permissions.ACTION_CAN_READ, permissions.RESOURCE_WEBSITE),
    ]

    class AppBuilderDagEditorView(BaseView):
        airflow_major_version = int(version.split('.')[0])
        route_base = ROUTE
        base_permissions = ['can_list', 'can_create', 'menu_acccess']

        @expose('/')
        @auth.has_access(PERMISSIONS)
        def list(self):
            return self._render('index')

        @expose('/files', methods=['GET'])
        @auth.has_access(PERMISSIONS)
        def root_ls(self):
            node = request.args.get('id')
            path = node if node != '#' else configuration.conf.get('core', 'dags_folder')

            return jsonify(
                TreeUtils.ls_to_tree_node(Storage.ls(path))
            )

        @expose("/read", methods=["GET"])
        @auth.has_access(PERMISSIONS)
        def read_file(self):
            path = request.args.get('path')
            return jsonify({
                'status': 'ok',
                'data': Storage.read(path)
            })

        @expose("/delete", methods=["POST"])
        @auth.has_access(PERMISSIONS)
        def delete_file(self):
            path = request.json.get('path')
            Storage.delete(path)
            return jsonify({
                'status': 'ok'
            })

        @expose("/save", methods=["POST"])
        @auth.has_access(PERMISSIONS)
        def save_file(self):
            path = request.json.get('path')
            data = request.json.get('data')
            Storage.write(path, data)
            return jsonify({
                'status': 'ok'
            })

        def _render(self, template, *args, **kargs):
            return self.render_template(
                template + '_appbuilder.html',
                airflow_major_version=self.airflow_major_version,
                js_files=JS_FILES,
                *args,
                **kargs
            )


except (ImportError, ModuleNotFoundError):
    from simple_dag_editor.auth import has_access
    from airflow.www_rbac.decorators import has_dag_access

    # AppBuilder (Airflow >= 1.10 < 2.0 and rbac = True)

    class AppBuilderDagEditorView(BaseView):
        airflow_major_version = int(version.split('.')[0])
        route_base = ROUTE
        base_permissions = ['can_list']

        @expose('/')
        @has_dag_access(can_dag_edit=True)
        @has_access
        def list(self):
            return self._render('index')

        @expose('/files', methods=['GET'])
        @has_dag_access(can_dag_edit=True)
        def root_ls(self):
            node = request.args.get('id')
            path = node if node != '#' else configuration.conf.get('core', 'dags_folder')

            return jsonify(
                TreeUtils.ls_to_tree_node(Storage.ls(path))
            )

        @expose("/read", methods=["GET"])
        @has_dag_access(can_dag_edit=True)
        @has_access
        def read_file(self):
            path = request.args.get('path')
            return jsonify({
                'status': 'ok',
                'data': Storage.read(path)
            })

        @expose("/delete", methods=["POST"])
        @has_dag_access(can_dag_edit=True)
        @has_access
        def delete_file(self):
            path = request.json.get('path')
            Storage.delete(path)
            return jsonify({
                'status': 'ok'
            })

        @expose("/save", methods=["POST"])
        @has_dag_access(can_dag_edit=True)
        @has_access
        def save_file(self):
            path = request.json.get('path')
            data = request.json.get('data')
            Storage.write(path, data)
            return jsonify({
                'status': 'ok'
            })

        def _render(self, template, *args, **kargs):
            return self.render_template(
                template + '_appbuilder.html',
                airflow_major_version=self.airflow_major_version,
                js_files=JS_FILES,
                *args,
                **kargs
            )


appbuilder_dag_editor_view = AppBuilderDagEditorView()
appbuilder_view = {
    'category': MENU_CATEGORY,
    'name': MENU_LABEL,
    'view': appbuilder_dag_editor_view,
}
