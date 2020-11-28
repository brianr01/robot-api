#!/usr/bin/env python
from flask import Flask, render_template, Response, Blueprint, request
import cv2
import sys
sys.path.append(sys.path[0] + '/Helpers')
from CamerasHelper import CamerasHelper

camerasController = Blueprint('camerasController', __name__)

cameras = CamerasHelper()

@camerasController.route('/video_feed_1')
def video_feed_1():
    return Response(cameras.generate_frame(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@camerasController.route('/video_feed_2')
def video_feed_2():
    return Response(cameras.generate_frame(1), mimetype='multipart/x-mixed-replace; boundary=frame')

@camerasController.route('/switch_video_feeds')
def switch_video_feeds():
    return Response(cameras.switch_cameras(), mimetype='multipart/x-mixed-replace; boundary=frame')
