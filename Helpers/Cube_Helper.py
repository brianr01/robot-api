from flask import Blueprint
from flask import request
import sys

sys.path.append(sys.path[0] + '/Helpers')
from Motors_Helper import Motors_Helper
from Virtual_Rubiks_Cube_Helper import Virtual_Rubiks_Cube_Helper

class Cube_Helper:
    def __init__(self):
        self.virtual_cube = Virtual_Rubiks_Cube_Helper()
        self.motors = Motors_Helper()
    
    def Turn(self, side, direction):
        self.virtual_cube.Turn_Side(side, direction)

        self.motors.Append_Direction_To_Action_String(direction)
        self.motors.Append_Turn_To_Action_String(side)

    def Power(self, state):
        self.motors.Append_Power_To_Action_String(state) 


    def Execute(self):
        self.motors.Send_Action_String()