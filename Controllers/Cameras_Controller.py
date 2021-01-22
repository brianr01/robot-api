#!/usr/bin/env python
from flask import Flask, render_template, Response, Blueprint, request
import cv2

import sys
sys.path.append(sys.path[0] + '/Helpers')
from Robot_Helper import robot

cameras_controller = Blueprint('cameras_controller', __name__)

@cameras_controller.route('/video_feed_1')
def Video_Feed_1():
    return Response(robot.cameras.Generate_Frame(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@cameras_controller.route('/video_feed_2')
def Video_Feed_2():
    return Response(robot.cameras.Generate_Frame(1), mimetype='multipart/x-mixed-replace; boundary=frame')

@cameras_controller.route('/switch_video_feeds')
def Switch_Video_Feeds():
    return Response(robot.cameras.Switch_Cameras(), mimetype='multipart/x-mixed-replace; boundary=frame')

@cameras_controller.route('/get_sticker_images')
def Get_Sticker_Images():
    return robot.cameras.Get_Sticker_Images()
    