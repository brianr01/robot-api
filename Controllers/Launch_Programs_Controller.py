#!/usr/bin/env python
from flask import Flask, render_template, Response, Blueprint, request
import cv2, sys, threading

sys.path.append(sys.path[0] + '/Helpers')
from Robot_Helper import robot

sys.path.append(sys.path[0] + '/Programs')
from Calibrate_Sticker_Location_Program import Calibrate_Sticker_Location_Program

launch_programs_controller = Blueprint('launch_programs_controller', __name__)


@launch_programs_controller.route('/launch_calibrate_sticker_location')
def Calibrate_Sticker_Location():
    global robot

    calibrate_sticker_location_program = Calibrate_Sticker_Location_Program()
    calibrate_sticker_location_program.Launch(
        robot.cameras.Get_Frames()
    )

    return 'Done'

