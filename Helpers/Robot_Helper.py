import sys
sys.path.append(sys.path[0] + '/Helpers')
from Cameras_Helper import Cameras_Helper
from Cube_Helper import Cube_Helper
import pickle, cv2, os, time, random

class Robot_Helper:
    def __init__(self):
        self.cube = Cube_Helper()
        self.cameras = Cameras_Helper()

    def Solve(self):
        predicted_cube_position = self.cameras.Get_Predicted_Cube_Colors()
        self.cube.virtual_cube.Set_Prediected_Cube_Position(predicted_cube_position)
        self.cube.virtual_cube.Orientate_Cube_For_Kociemba()
        self.cube.Solve_Cube_With_Tracked_Position()

    def Generate_Cube_Training_Images(self):
        path = self.Create_New_Sticker_Directory()
        self.cube.virtual_cube.Reset()
        self.cube.Power('on')
        self.cube.Execute()

        for i in range(0, 200):
            print(i)
            self.cube.Do_Random_Moves_While_Tracking_Cube(5)
            self.Generate_One_Training_Image_Set(path)
        
        self.cube.Solve_Cube_With_Tracked_Position()


    def Create_New_Sticker_Directory(self):
        path = 'Images/Saves/stickers-' + str(round(time.time()))
        os.mkdir(path)
        for side in self.cube.virtual_cube.side_order:
            os.mkdir(path + '/' + side)

        return path

    def Generate_One_Training_Image_Set(self, path):
        sticker_images = self.cameras.Get_Sticker_Images()
        cube_position = self.cube.virtual_cube.Get_Cube_Position_For_Training_Images()
        
        for image, color in zip(sticker_images, cube_position):
            cv2.imwrite(path + '/' + color + '/' + color + '-' + str(time.time()) + '-sticker.jpg', image)

robot = Robot_Helper()