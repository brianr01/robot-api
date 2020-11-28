from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from TurnController import cube


cubeController = Blueprint('CubeController', __name__)

@cubeController.route("/get_cube_position")
def Get_Cube_Position():
    global cube
    return cube.virtual_cube.get_cube_state()