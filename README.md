# simple-dag-editor

[![PyPI version](https://badge.fury.io/py/simple-dag-editor.svg)](https://badge.fury.io/py/simple-dag-editor)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/simple-dag-editor)](https://pypi.org/project/simple-dag-editor/)
[![License](https://img.shields.io/:license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)

SimpleDagEditor is a zero configuration plugin for [Apache Airflow](https://github.com/apache/airflow).
It provides a file managing interface that points to your dag_folder directory.
With this plugin you will be able to delete, duplicate & edit you dags.

### System Requirements

* Airflow 1.10.x
* Not tested for Airflow 2.x

### Manual Installation
1. Copy 'simple_dag_editor' folder into your plugins directory
2. Restart airflow instance
3. Open Admin - Simple DAG editor

### Package Installation
1. Install the plugin (pip install simple-dag-editor)
2. Restart airflow instance
3. Open Admin - Simple DAG editor

### Optional configurations
* [dag_editor] - disabled (Default - False)
    
### Screenshots


![Main editor screen](https://raw.githubusercontent.com/ohadmata/simple-dag-editor/main/screenshots/image1.png)
![Save as modal](https://raw.githubusercontent.com/ohadmata/simple-dag-editor/main/screenshots/image2.png)
![Save confirm](https://raw.githubusercontent.com/ohadmata/simple-dag-editor/main/screenshots/image3.png)

