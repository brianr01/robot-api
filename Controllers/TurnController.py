from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from CubeHelper import CubeHelper

cube = CubeHelper()

turnController = Blueprint('turnController', __name__)

@turnController.route("/power")
def Power():
    global cube
    state = request.args.get('state')

    cube.Power(state)
    cube.Execute()

    return state

@turnController.route("/turn")
def Turn_Side():
    global cube
    side = request.args.get('side')
    direction = request.args.get('direction')

    cube.Power('True')        # Power on
    cube.Turn(side, direction)
    cube.Power('False')       # Power off

    cube.Execute()

    return 'done'

@turnController.route("/scramble")
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

@turnController.route("/solve")
def Solve():
    global cube

    solution = cube.virtual_cube.get_solution()

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
