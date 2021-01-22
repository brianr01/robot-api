import cv2, os, sys, math, pickle
import numpy as np
CATEGORIES = ['white','yellow','orange','red','green','blue']

import tensorflow as tf
model = tf.keras.models.load_model("cube_ai_model_9996")

class Cameras_Helper:
    def __init__(self):
        self.cameras = []
        self.Get_valid_Cameras()
        if len(self.cameras) < 2:
            raise Exception("There are not enough cameras to run. Only " + str(len(self.cameras)) + " cameras detected.")

    def Get_valid_Cameras(self):
        for i in range(5):
            cap = self.Test_Device(i)
            if (cap):
                print("Found camera. It is on device video " + str(i) + ".")
                self.cameras.append(cap)
            
            if len(self.cameras) == 2:
                break

    def Test_Device(self, source):
        cap = cv2.VideoCapture(source) 
        if cap is None or not cap.isOpened():
            return None
        
        return cap

    def Get_Frame(self, camera_number):
        success, frame = self.cameras[camera_number].read()

        return frame
    
    def Get_Frames(self):
        frames = []
        for camera_number in range(0, len(self.cameras)):
            frames.append(self.Get_Frame(camera_number))

        return frames

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

    def Get_Sticker_Images(self):
        sticker_images = []
        frames = self.Get_Frames()
        
        point_saves = pickle.load(open( "Saves/Points_Saves.p", "rb"))

        for i, point in enumerate(point_saves):
            frame = frames[self.Get_Camera_Number(i)]
            sticker_images.append(
                self.Get_Sticker_Image(point, frame)
            )
        
        return sticker_images
    
    def Get_Sticker_Image(self, point, frame):
        copy_frame = frame.copy()
        return copy_frame[ 
            point[1] - 25: point[1] + 25,
            point[0] - 25: point[0] + 25
        ]
        

    def Get_Predicted_Cube_Colors(self):
        sticker_images = self.Get_Sticker_Images()
        colors = []
        for image in sticker_images:
            colors.append(self.Predict_Cube_Color(image))
    
        return colors

    def Predict_Cube_Color(self, image):
        formatted_image = self.Format_Image_For_Color_Prediction(image)

        
        # Predict
        predictions = model.predict([formatted_image])[0].tolist()
        prediction = CATEGORIES[predictions.index(max(predictions))]

        return prediction

    def Format_Image_For_Color_Prediction(self, image):
        return np.array((image / 255.0)).reshape(-1, 50, 50, 3)

    def Get_Camera_Number(self, sticker_number):
        side_order = 'urfdlb'
        camera_sides = ['ubr', 'ldf']
        return 1 if side_order[math.floor(sticker_number / 9)] in camera_sides[0] else 0
            

