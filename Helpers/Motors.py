import serial

class Motors:
    side_letter_to_character_dictionary = {
        'r':'e',
        'l':'f',
        'u':'g',
        'd':'h',
        'f':'i',
        'b':'j'
    }

    direction_to_character_dictionary = {
        'c': 'c',
        'ccw': 'g'
    }

    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        self.actionString = ''

    def Append_Power_To_Action_String(self, state):
        character = 'a' if state == 'True' else 'b'
        self.actionString += character
    
    def Append_Direction_To_Action_String(self, direction):
        self.actionString += self.direction_to_character_dictionary[direction]
    
    def Append_Turn_To_Action_String(self, side):
        self.actionString += self.side_letter_to_character_dictionary[side]            

    def Append_End_To_Action_String(self):
        self.actionString += '|'

    def Send_Action_String(self):
        self.Append_End_To_Action_String()

        for character in self.actionString:
            self.arduino.write(character.encode('UTF-8'))
        
        self.actionString = ''