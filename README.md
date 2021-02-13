# Robot API

A python api to control Rubik's cube solving robot using flask.

## Requirements

* [Python 3](https://www.python.org/downloads/)
* [Pip 3](https://www.educative.io/edpresso/installing-pip3-in-ubuntu)
* [Virtual Env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Installation

1. Create a new directory and pull repository.
2. Create a new environment.
```bash
conda env create --file environment.yml
```
3. Activate the new environment.
```bash
conda activate robot-env
```
## Startup
### Option 1 Makefile
1. Run `make up`
### Option 2 Manually
1. Change the permissions on the connected arduino.
```bash
sudo chmod 777 /dev/ttyACM0
```
2. Activate virtual environment.
```bash
conda activate robot-envco
```
3. Start the api.
```bash
python3 app.py
```

## Calibrate

### Sticker Boxes
1. Actiate virtual environment.
```bash
source env/bin/activate
```
2.Launch Program.
```bash
python Launch_Calibrate_Sticker_Location.py
```
3.Controls (information)
(Click) TO change current location.
Q: Go to previous sticker.
E: GO to next sticker.
V: Load current save.
C: Save current points.
W: Move box up a few pixels.
S: Move box down a few pixels.
D: Move Box right a few pixels.
A: Move Box left a few pixels.
ESC: Hold for at most 10 seconds to stop program.
4.Windows (information)
Reference: Use this window to see where to place sticker box.
Calibration: Use this window to calibrate the sticker box and use other controls.
