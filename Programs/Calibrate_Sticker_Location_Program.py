import cv2, sys, math, time, pickle

class Calibrate_Sticker_Location_Program:
    def __init__(self):
        self.points = []
        for i in range (0, 54):
            self.points.append([150,150])
        self.side_order = 'rludfb'
        self.camera_sides = ['ubr', 'ldf']
        self.current_sticker = 0
        self.current_session_saved = False
        self.times_escape_hit = 0
        self.cube_reference_points_dictionary = {
            'f':[
                [97,189],
                [60,181],
                [28,161],
                [95,151],
                [57,137],
                [24,119],
                [93,106],
                [57,88],
                [22,75]],
            'b':[
                [131,105],
                [164,86],
                [201,68],
                [133,152],
                [166,134],
                [201,112],
                [133,199],
                [169,177],
                [201,158]],
            'u':[
                [180,37],
                [146,55],
                [112,71],
                [144,25],
                [111,39],
                [75,55],
                [108,10],
                [75,24],
                [38,41]],
            'd':[
                [112,71],
                [75,55],
                [38,41],
                [146,55],
                [111,39],
                [75,24],
                [180,37],
                [144,25],
                [108,10]],
            'l':[
                [201,158],
                [169,177],
                [133,199],
                [201,112],
                [166,134],
                [133,152],
                [201,68],
                [164,86],
                [131,105]],
            'r':[
                [22,75],
                [57,88],
                [93,106],
                [24,119],
                [57,137],
                [95,151],
                [28,161],
                [60,181],
                [97,189]
            ]}

    def Launch(self, frame_0, frame_1):
        self.frames = [frame_0, frame_1]
        while True:
            cv2.imshow('view', self.Get_Cube_Calibration_Segment(self.current_sticker))
            cv2.imshow('frame', self.Get_Frame_With_Sticker_Box())
            cv2.setMouseCallback('frame', self.Update)
            k = cv2.waitKey(33)
            if k==27:    # Esc key to stop
                print('Escape')
                print(self.times_escape_hit)
                if self.current_session_saved or self.times_escape_hit == 100:
                    break
                
                self.times_escape_hit += 1
            elif k == 119:
                print('w')
                self.points[self.current_sticker][1] -= 1
            elif k == 115:
                print('s')
                self.points[self.current_sticker][1] += 1
            elif k == 97:
                print('a')
                self.points[self.current_sticker][0] -= 1
            elif k == 100:
                print('d')
                self.points[self.current_sticker][0] += 1
            elif k == 113:
                print('q')
                self.current_sticker -= 1
                self.current_sticker %=  54
                print(self.Convert_Decimal_To_Sticker_Address(self.current_sticker))
            elif k == 101:
                print('e')
                self.current_sticker += 1
                self.current_sticker %= 54
                print(self.Convert_Decimal_To_Sticker_Address(self.current_sticker))
            elif k == 99:
                print('c')
                self.Save_Points()
            elif k == 118:
                print('v')
                self.Load_Points()
            elif k==-1:  # normally -1 returned,so don't print it
                continue
            else:
                print(k) # else print its value
        cv2.destroyAllWindows()

    def Save_Points(self):
        self.Create_Backup_Of_Previous_Save()
        pickle.dump(self.points, open( "Saves/Points_Saves.p", "wb" ))
        self.current_session_saved = True

    def Create_Backup_Of_Previous_Save(self):
        try:
            previous_save = pickle.load(open( "Saves/Points_Saves.p", "rb" ))
            pickle.dump(previous_save, open( "Saves/Points_Saves" + str(math.floor(time.time())) + ".p", "wb" ))
        except Exception as e:
            print('Error: unable to create backup.')

    def Load_Points(self):
        self.points = pickle.load(open( "Saves/Points_Saves.p", "rb" ))        
    
    def Update(self, event, y, x, flag, flag2):
        if event == 4:
            self.points[self.current_sticker] = [y, x]
            print(self.points)

    def Get_Frame_With_Sticker_Box(self):
        frame = self.Get_Correct_Frame().copy()

        box_point = self.points[self.current_sticker]

        return cv2.rectangle(
            frame,
            (box_point[0] - 25, box_point[1] - 25), (box_point[0] + 25, box_point[1] + 25),
            (0, 0, 0),
            3
        )

    def Get_Correct_Frame(self):
        if self.Get_Current_Side_Letter() in self.camera_sides[0]:
            return self.frames[0]

        return self.frames[1]

    def Get_Current_Side_Letter(self):
        return self.Convert_Decimal_To_Sticker_Address(self.current_sticker)[0]

    def Convert_Decimal_To_Sticker_Address(self, decimal):
        decimal = decimal % (6 * 9)

        current_side_number = math.floor(decimal / 9)
        current_side_letter = self.side_order[current_side_number]
        current_sticker_number = decimal % 9

        return current_side_letter + str(current_sticker_number)        
    
    def Get_Cube_Calibration_Segment(self, decimal):
            address = self.Convert_Decimal_To_Sticker_Address(decimal)
            image = cv2.imread(sys.path[0] + '/Images/cube_reference_image.jpeg')
            point = self.cube_reference_points_dictionary[address[0]][int(address[1])]
            point = (point[0], point[1])
            cv2.circle(image, point, 10, (90,255,0), -1)

            return image
