import airflow
from airflow import configuration
from airflow.version import version
from functools import wraps
from flask import jsonify, request
from simple_dag_editor.commons import ROUTE, MENU_CATEGORY, MENU_LABEL
from simple_dag_editor.utils import Storage, TreeUtils

__all__ = ["admin_view"]

# AppBuilder (Airflow < 2.0)

try:
    from flask_admin import BaseView, expose
    AIRFLOW_MAJOR_VERSION = int(version.split('.')[0])

    def login_required(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            if airflow.login:
                return airflow.login.login_required(func)(*args, **kwargs)
            return func(*args, **kwargs)

        return func_wrapper

    class AdminDagEditorView(BaseView):
        @expose("/")
        @login_required
        def index(self):
            return self._render('index')

        @expose("/files", methods=["GET"])
        @login_required
        def root_ls(self):
            node = request.args.get('id')
            path = node if node != '#' else configuration.conf.get('core', 'dags_folder')

            return jsonify(
                TreeUtils.ls_to_tree_node(Storage.ls(path))
            )

        @expose("/read", methods=["GET"])
        @login_required
        def read_file(self):
            path = request.args.get('path')
            return jsonify({
                'status': 'ok',
                'data': Storage.read(path)
            })

        @expose("/delete", methods=["POST"])
        @login_required
        def delete_file(self):
            path = request.json.get('path')
            Storage.delete(path)
            return jsonify({
                'status': 'ok'
            })

        @expose("/save", methods=["POST"])
        @login_required
        def save_file(self):
            path = request.json.get('path')
            data = request.json.get('data')
            Storage.write(path, data)
            return jsonify({
                'status': 'ok'
            })

        def _render(self, template, *args, **kwargs):
            return self.render(
                template + "_admin.html",
                airflow_major_version=AIRFLOW_MAJOR_VERSION,
                *args,
                **kwargs
            )

    admin_view = AdminDagEditorView(url=ROUTE, category=MENU_CATEGORY, name=MENU_LABEL)

except (ImportError, ModuleNotFoundError):
    admin_view = None
