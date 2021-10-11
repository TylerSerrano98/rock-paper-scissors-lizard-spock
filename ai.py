from players import Players
import random

class AI(Players):
    def __init__(self):
        super().__init__("robot")
       
        

    def gesture(self):
        self.choice_gesture = random.choice(self.human_gestures)
        # if self.choice_gesture  in  self.ai_gesture:
        #     print(self.choice_gesture)
        # else:
        #     while self.gesture_select not in self.ai_gestures:
        #         print("/n not a choice.. Please select: rock, papers, scissors, lizard, sock/n")
                

        print (f'gesure choosen: {self.choice_gesture}')
    def set_name(self):
        self.property_name = 'robot'
        print(self.property_name)


      