from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from Turn_Controller import cube


cube_controller = Blueprint('cube_controller', __name__)

@cube_controller.route("/get_cube_position")
def Get_Cube_Position():
    global cube
    return cube.virtual_cube.Get_Cube_State()