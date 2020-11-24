from flask import Blueprint
from flask import request
import serial
import sys
sys.path.append(sys.path[0] + '/Helpers')
from Motors import Motors


turnController = Blueprint('turnController', __name__)

motors = Motors()

@turnController.route("/power")
def Power():
    global motors
    state = request.args.get('state')

    motors.Append_Power_To_Action_String(state)
    motors.Send_Action_String()

    return state

@turnController.route("/turn")
def Turn_Side():
    global motors
    side = request.args.get('side')
    direction = request.args.get('direction')

    motors.Append_Power_To_Action_String('True')        # Power on
    motors.Append_Direction_To_Action_String(direction) # Direction
    motors.Append_Turn_To_Action_String(side)           # Turn side
    motors.Append_Direction_To_Action_String('c')       # Direction clock wise
    motors.Append_Power_To_Action_String('False')       # Power off

    motors.Send_Action_String()

    return 'done'
