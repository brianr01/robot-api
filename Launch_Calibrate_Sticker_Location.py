#!/usr/bin/env python
import cv2, sys, threading

sys.path.append(sys.path[0] + '/Helpers')
from Robot_Helper import robot

sys.path.append(sys.path[0] + '/Programs')
from Calibrate_Sticker_Location_Program import Calibrate_Sticker_Location_Program

calibrate_sticker_location_program = Calibrate_Sticker_Location_Program()
calibrate_sticker_location_program.Launch(
    robot.cameras.Get_Frames()[::-1]
)
