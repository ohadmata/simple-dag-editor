__all__ = [
    'PLUGIN_NAME',
    'MENU_CATEGORY',
    'MENU_LABEL',
    'ROUTE',
    'STATIC',
    'JS_FILES'
]

PLUGIN_NAME = 'dag_editor'
MENU_CATEGORY = 'Admin'
MENU_LABEL = 'Simple DAG editor'
ROUTE = '/' + PLUGIN_NAME
STATIC = '/static/' + PLUGIN_NAME
JS_FILES = [
    'js/ace.min.js',
    'js/jstree.min.js',
    'js/mode-python.min.js',
    'js/sweetalert2.all.min.js'
]
