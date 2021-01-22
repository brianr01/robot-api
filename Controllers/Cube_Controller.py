from flask import Blueprint
from flask import request
import serial, random

import sys
sys.path.append(sys.path[0] + '/Helpers')
from Robot_Helper import robot

cube_controller = Blueprint('cube_controller', __name__)

@cube_controller.route("/get_cube_position")
def Get_Cube_Position():
    global robot
    return robot.cube.virtual_cube.Get_Cube_State()

@cube_controller.route("/generate_training_images")
def Generate_Cube_Training_Images():
    global robot

    robot.Generate_Cube_Training_Images()
    return 'Done'