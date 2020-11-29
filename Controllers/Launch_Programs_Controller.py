#!/usr/bin/env python
from flask import Flask, render_template, Response, Blueprint, request
import cv2, sys, threading
sys.path.append(sys.path[0] + '/Controllers')
from Cameras_Controller import cameras
sys.path.append(sys.path[0] + '/Programs')
from Calibrate_Sticker_Location_Program import Calibrate_Sticker_Location_Program

launch_programs_controller = Blueprint('launch_programs_controller', __name__)



@launch_programs_controller.route('/launch_calibrate_sticker_location')
def Calibrate_Sticker_Location():
    global cameras
    frame_0 = cameras.Get_Frame(0)
    frame_1 = cameras.Get_Frame(1)
    calibrate_sticker_location_program = Calibrate_Sticker_Location_Program()
    t1 = threading.Thread(target=calibrate_sticker_location_program.Launch, args=(frame_0, frame_1)) 
    t1.start()
    return 'Done'

