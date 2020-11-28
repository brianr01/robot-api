import cv2
import os
import sys

class Cameras_Helper:
    def __init__(self):
        self.cameras = []
        self.Get_valid_Camera()

    def Get_valid_Camera(self):
        for i in range(5):
            cap = self.Test_Device(i)
            if (cap):
                print(i)
                self.cameras.append(cap)
            
            if len(self.cameras) == 2:
                break

    def Test_Device(self, source):
        cap = cv2.VideoCapture(source) 
        if cap is None or not cap.isOpened():
            return None
        
        return cap

    def Generate_Frame(self, camera_number):
        while True:
            success, frame = self.cameras[camera_number].read()

            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    
    def Switch_Cameras(self):
        self.cameras = self.cameras[::-1]
