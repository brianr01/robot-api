from flask import Blueprint
from flask import request
import sys, random, time

sys.path.append(sys.path[0] + '/Helpers')
from Motors_Helper import Motors_Helper
from Virtual_Rubiks_Cube_Helper import Virtual_Rubiks_Cube_Helper

class Cube_Helper:
    def __init__(self):
        self.virtual_cube = Virtual_Rubiks_Cube_Helper()
        self.motors = Motors_Helper()
    
    def Turn(self, side, direction):
        self.virtual_cube.Turn_Side(side, direction)
        self.motors.Append_Turn_To_Action_String(side, direction)

    def Power(self, state):
        self.motors.Append_Power_To_Action_String(state) 

    def Execute(self):
        self.motors.Send_Action_String()

    def Do_Random_Moves_While_Tracking_Cube(self, move_count):
        for i in range(0, move_count):
            self.Append_Random_Move()
        self.Execute()
        time.sleep(move_count * .15)

    def Append_Random_Move(self):
        self.Turn(
            self.Get_Random_Side(),
            self.Get_Random_Direction()
        )

    def Get_Random_Side(self):
        return random.choice('urfdlb')

    def Get_Random_Direction(self):
        return random.choice(['c', 'ccw'])

    def Solve_Cube_With_Tracked_Position(self):
        solution = self.virtual_cube.Get_Solution()
        
        self.Execute_Moves_With_Normal_Notation(solution)

    def Execute_Moves_With_Normal_Notation(self, moves):
        moves = moves.split(" ")

        self.Power('on')

        for move in moves:
            self.Execute_Single_Move_With_Normal_Notation(move)
        
        self.Power('off')
        self.Execute()

    def Execute_Single_Move_With_Normal_Notation(self, move):
        direction = 'c'
        if "'" in move:
            direction = 'ccw'

        if "2" in move:
            self.Turn(move[0].lower(), direction)

        self.Turn(move[0].lower(), direction)
