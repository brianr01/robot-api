from flask import Blueprint
from flask import request
import sys

sys.path.append(sys.path[0] + '/Helpers')
from MotorsHelper import MotorsHelper
from VirtualRubiksCubeHelper import VirtualRubiksCubeHelper

class CubeHelper:
    def __init__(self):
        self.virtual_cube = VirtualRubiksCubeHelper()
        self.motors = MotorsHelper()
    
    def Turn(self, side, direction):
        self.virtual_cube.turn_side(side, direction)

        self.motors.Append_Direction_To_Action_String(direction)
        self.motors.Append_Turn_To_Action_String(side)

    def Power(self, state):
        self.motors.Append_Power_To_Action_String(state) 


    def Execute(self):
        self.motors.Append_Direction_To_Action_String('c')
        self.motors.Append_Power_To_Action_String('False')

        self.motors.Send_Action_String()