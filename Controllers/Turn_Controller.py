from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from Robot_Helper import robot


turn_controller = Blueprint('turn_controller', __name__)


@turn_controller.route("/power")
def Power():
    global robot
    state = request.args.get('state')

    robot.cube.Power(state)
    robot.cube.Execute()

    return state

@turn_controller.route("/turn")
def Turn_Side():
    global robot
    side = request.args.get('side')
    direction = request.args.get('direction')

    robot.cube.Power('on')
    robot.cube.Turn(side, direction)
    robot.cube.Power('off')

    robot.cube.Execute()

    return 'done'

@turn_controller.route("/scramble")
def Scramble():
    global robot

    robot.cube.Power('on')
    robot.cube.Do_Random_Moves_While_Tracking_Cube(30)

    robot.cube.Power('off')
    robot.cube.Execute()

    return 'done'

@turn_controller.route("/solve")
def Solve():
    global robot

    robot.Solve()

    return 'solving'
