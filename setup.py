#!/usr/bin/env python
import os
import os.path
import re
import glob
from setuptools import find_packages, setup
from itertools import chain

VERSION_RE = re.compile("__version__\\s*=\\s*['\"](.*)['\"]")
PLUGIN_NAME = 'simple_dag_editor'
PLUGIN_ROOT_FILE = 'simple_dag_editor.py'
PLUGIN_ENTRY_POINT = 'SimpleDagEditor'


def get_version():
    with open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            f"{PLUGIN_NAME}/{PLUGIN_ROOT_FILE}",
        )
    ) as f:
        for line in f:
            match = VERSION_RE.match(line)
            if match:
                return match.group(1)
    raise Exception


def get_package_data():
    exts = ["js", "css", "html", "svg", "png", "jpg", "gif"]
    files = list(
        chain(
            *[
                glob.glob(f"{PLUGIN_NAME}/**/*.%s" % x, recursive=True)
                for x in exts
            ]
        )
    )
    return [x.split("/", 1)[1] for x in files]


with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().split("\n")

setup(
    name=PLUGIN_NAME,
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    package_data={PLUGIN_NAME: get_package_data()},
    entry_points={
        "airflow.plugins": [
            f"{PLUGIN_NAME} = {PLUGIN_NAME}.{PLUGIN_NAME}:{PLUGIN_ENTRY_POINT}"
        ]
    },
    zip_safe=False,
    url="https://github.com/ohadmata/simple-dag-editor",
    author="Ohad mata",
    author_email="ohadmata@gmail.com",
    description="Zero configuration Airflow Dag editor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    license="Apache License, Version 2.0",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
