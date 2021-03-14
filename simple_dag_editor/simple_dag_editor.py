#!/usr/bin/env python
#
#   Copyright 2021 Ohad mata <ohadmata@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License
#
__author__ = 'Ohad Mata <ohadmata@gmail.com>'
__version__ = '0.1.0'

from flask import Blueprint
from airflow.plugins_manager import AirflowPlugin
from airflow import configuration
from simple_dag_editor.commons import STATIC
from simple_dag_editor.flask_admin_view import admin_view
from simple_dag_editor.app_builder_view import appbuilder_view

__all__ = ['SimpleDagEditor']

simple_dag_editor_blueprint = Blueprint(
    'simple_dag_editor_blueprint',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path=STATIC,
)


class SimpleDagEditor(AirflowPlugin):
    name = 'simple_dag_editor'
    operators = []
    hooks = []
    executors = []
    menu_links = []

    if configuration.getboolean('dag_editor', 'DISABLED', fallback=False):
        flask_blueprints = []
        admin_views = []
        appbuilder_views = []
    else:
        flask_blueprints = [simple_dag_editor_blueprint]
        admin_views = [admin_view] if admin_view is not None else []
        appbuilder_views = [appbuilder_view]
