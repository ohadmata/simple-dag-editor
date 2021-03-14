import os
from typing import List, Dict


class Storage:

    @classmethod
    def ls(cls, path: str) -> List[Dict[str, str]]:
        result = list()
        for n in os.listdir(path):
            if os.path.isdir(os.path.join(path, n)):
                result.append({'name': n, 'type': 'folder', 'path': path + '/' + n})
            else:
                result.append({'name': n, 'type': 'file', 'path': path + '/' + n})
        return result

    @classmethod
    def read(cls, path: str) -> str:
        with open(path, 'r') as f:
            data = f.read()
        return data

    @classmethod
    def exists(cls, path: str) -> bool:
        return os.path.exists(path)

    @classmethod
    def delete(cls, path: str):
        if cls.exists(path):
            os.remove(path)

    @classmethod
    def write(cls, path: str, content: str):
        with open(path, 'w') as f:
            f.write(content)


class TreeUtils:

    @staticmethod
    def ls_to_tree_node(nodes: List[Dict[str, str]]) -> List[Dict[str, str]]:
        result = list()
        for n in nodes:
            result.append({
                'id': n.get('path'),
                'text': n.get('name'),
                'children': True if n.get('type') == 'folder' else False,
                'icon': 'jstree-folder' if n.get('type') == 'folder' else 'jstree-file'
            })
        return result
