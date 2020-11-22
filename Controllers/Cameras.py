#!/usr/bin/env python
from flask import Flask, render_template, Response, Blueprint, request
import cv2

cameras = Blueprint('cameras', __name__)

camera1 = cv2.VideoCapture(1)
camera2 = cv2.VideoCapture(3)

def Generate_Frames_1():  
    while True:
        success, frame = camera2.read()

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

def Generate_Frames_2():  
    while True:
        success, frame = camera1.read()

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@cameras.route('/video_feed_1')
def video_feed_1():
    return Response(Generate_Frames_1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@cameras.route('/video_feed_2')
def video_feed_2():
    return Response(Generate_Frames_2(), mimetype='multipart/x-mixed-replace; boundary=frame')
