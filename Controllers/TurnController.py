from flask import Blueprint
from flask import request
import serial, sys, random
sys.path.append(sys.path[0] + '/Helpers')
from MotorsHelper import Motors
from CubeController import cube

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
    global motors, cube
    side = request.args.get('side')
    direction = request.args.get('direction')

    motors.Append_Power_To_Action_String('True')        # Power on
    motors.Append_Direction_To_Action_String(direction) # Direction
    motors.Append_Turn_To_Action_String(side)           # Turn side
    motors.Append_Direction_To_Action_String('c')       # Direction clock wise
    motors.Append_Power_To_Action_String('False')       # Power off

    motors.Send_Action_String()

    turn_clock_wise = direction == 'c'
    cube.turn_side(side, turn_clock_wise)
    return 'done'

@turnController.route("/scramble")
def Scramble():
    global motors, cube

    motors.Append_Power_To_Action_String('True')
    for i in range(0,30):
        side = random.choice('rludfb')
        direction = random.choice(['c', 'ccw'])

        turn_clock_wise = direction == 'c'
        print(turn_clock_wise)
        cube.turn_side(side, turn_clock_wise)

        motors.Append_Direction_To_Action_String(direction)
        motors.Append_Turn_To_Action_String(side)

    motors.Append_Direction_To_Action_String('c')
    motors.Append_Power_To_Action_String('False')

    motors.Send_Action_String()

    return 'done'

@turnController.route("/solve")
def Solve():
    global motors, cube

    solution = cube.get_solution()

    solution = solution.split()

    motors.Append_Power_To_Action_String('True') 

    for move in solution:
        move += ' '
        side = move[0].lower()
        direction =  'c' if move[1] != "'" else 'ccw'
        motors.Append_Direction_To_Action_String(direction)
        motors.Append_Turn_To_Action_String(side)

        turn_clock_wise = direction == 'c'
        cube.turn_side(side, turn_clock_wise)
        if move[1] == '2':
            cube.turn_side(side, turn_clock_wise)
            motors.Append_Turn_To_Action_String(side)
    
    motors.Append_Power_To_Action_String('False') 
    motors.Send_Action_String()

    return {'value': solution}
