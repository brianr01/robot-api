# Robot API

A python api to control Rubik's cube solving robot using flask.

## Requirements

* [Python 3](https://www.python.org/downloads/)
* [Pip 3](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)
* [Virtual Env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Installation

1. Create a new directory and pull repository.
2. Create a new environment.
```bash
python3 -m venv env
```
3. Activate the new environment.
```bash
source env/bin/activate
```
4. Update pip.
```bash
pip3 install --upgrade pip
```
4. Install the required python modules.
```bash
pip3 install -r requirements.txt
```

## Startup

1. Change the permissions on the connected arduino.
```bash
sudo chmod 777 /dev/ttyACM0
```
2. Activate virtual environment.
```bash
source env/bin/activate
```
3. Start the api.
```bash
python3 app.py
```

