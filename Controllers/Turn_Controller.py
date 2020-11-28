from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from Cube_Helper import Cube_Helper

cube = Cube_Helper()

turn_controller = Blueprint('turn_controller', __name__)

@turn_controller.route("/power")
def Power():
    global cube
    state = request.args.get('state')

    cube.Power(state)
    cube.Execute()

    return state

@turn_controller.route("/turn")
def Turn_Side():
    global cube
    side = request.args.get('side')
    direction = request.args.get('direction')

    cube.Power('True')        # Power on
    cube.Turn(side, direction)
    cube.Power('False')       # Power off

    cube.Execute()

    return 'done'

@turn_controller.route("/scramble")
def Scramble():
    global cube

    cube.Power('True')
    for i in range(0,30):
        side = random.choice('rludfb')
        direction = random.choice(['c', 'ccw'])

        cube.Turn(side, direction)

    cube.Power('False')

    cube.Execute()

    return 'done'

@turn_controller.route("/solve")
def Solve():
    global cube

    solution = cube.virtual_cube.Get_Solution()

    solution = solution.split()

    cube.Power("True")
    for move in solution:
        move += ' '
        side = move[0].lower()
        direction =  'c' if move[1] != "'" else 'ccw'
        cube.Turn(side, direction)
        if move[1] == '2':
            cube.Turn(side, direction)
    
    cube.Power("False")
    cube.Execute()

    return {'value': solution}
