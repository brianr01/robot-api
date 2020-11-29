import cv2, os, sys, math, pickle

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

    def Get_Frame(self, camera_number):
        success, frame = self.cameras[camera_number].read()

        return frame

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
        frames = [self.Get_Frame(0), self.Get_Frame(1)]
        
        point_saves = pickle.load(open( "Saves/Points_Saves.p", "rb"))

        for i in range(len(point_saves)):
            point = point_saves[i]
            print(self.Get_Camera_Number(i))
            copy_frame = frames[self.Get_Camera_Number(i)].copy()
            print([point[0] - 25, point[1] - 25, 
                    point[0] + 25, point[1] + 25])
            sticker_images.append(
                copy_frame[ 
                    point[1] - 25: point[1] + 25,
                    point[0] - 25: point[0] + 25
                ]
            )

        # number = 0
        
        # print(len(sticker_images))
        # while True:
        #     if number == 54:
        #         break
        #     cv2.imshow('frame0', frames[0])
        #     cv2.imshow('frame1', frames[1])
        #     cv2.imshow('frame', sticker_images[number])
        #     k = cv2.waitKey(33)
        #     if k==27:
        #         break
        #     elif k!=-1:
        #         number += 1
        #         print(number)

        # cv2.destroyAllWindows()
        return sticker_images
    
    def Get_Camera_Number(self, sticker_number):
        side_order = 'rludfb'
        camera_sides = ['ubr', 'ldf']
        return 1 if side_order[math.floor(sticker_number / 9)] in camera_sides[0] else 0
            

