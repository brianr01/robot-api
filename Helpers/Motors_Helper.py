import serial, time

class Motors_Helper:
    opposite_side_action_letters_dictionary ={   
        'e' : 'f',
        'f' : 'e',
        'g' : 'h',
        'h' : 'g',
        'i' : 'j',
        'j' : 'i'
    }

    side_letter_to_character_dictionary = {
        'r':'e',
        'l':'f',
        'u':'g',
        'd':'h',
        'f':'i',
        'b':'j'
    }

    turn_characters = 'efghij'

    direction_to_character_dictionary = {
        'c': 'c',
        'ccw': 'd'
    }

    power_to_character_dictionary = {
        'on': 'a',
        'off': 'b'
    }

    move_optimization_dictionary = {
        'ef' : 'k',
        'Ef' : 'K',
        'eF' : 'l',
        'EF' : 'L',
        'gh' : 'm',
        'Gh' : 'M',
        'gH' : 'n',
        'GH' : 'N',
        'ij' : 'o',
        'Ij' : 'O',
        'iJ' : 'p',
        'IJ' : 'P',
    }

    def __init__(self):
        print('init motors')
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        self.actionString = ''

    def Append_Power_To_Action_String(self, state):
        self.actionString += self.power_to_character_dictionary[state]
    
    def Append_Direction_To_Action_String(self, direction):
        self.actionString += self.direction_to_character_dictionary[direction]
    
    def Append_Turn_To_Action_String(self, side, direction):
        character = self.side_letter_to_character_dictionary[side] 
        if (direction == 'c'):
            self.actionString += character
        else:
            self.actionString += character.upper()           

    def Append_End_To_Action_String(self):
        self.actionString += '|'

    def Send_Action_String(self):
        self.Append_End_To_Action_String()
        print(self.actionString)
        self.Optimize_Action_String()
        print(self.actionString)
        for character in self.actionString:
            time.sleep(.004)
            self.arduino.write(character.encode('UTF-8'))
        
        self.actionString = ''

    def Optimize_Action_String(self):
        for expanded, simplified in self.move_optimization_dictionary.items():
            self.actionString = self.actionString.replace(expanded, simplified)
            self.actionString =  self.actionString.replace(expanded[::-1], simplified)




    