from players import Players
import random

class AI(Players):
    def __init__(self):
        self.choose_gesture = ''
        super().__init__()
        self.set_name()
        

    def gesture(self):
        self.select_gesture = input('/n Please enter: rock, paper, scissors, lizard, spock\n')
        if self.gesture_select  in  self.ai_gestures:
            print(random.choice(self))
        else:
            while self.gesture_select not in self.ai_gestures:
                print("/n not a choice.. Please select: rock, papers, scissors, lizard, sock/n")
                self.choice = input("/nPlease enter: rock, paper, scissors, lizard, spock\n" )

        print (f'gesure choosen: {self.gesture_select}')


    def set_name(self):
        robot = self.name
        print(self.name)
        self.set_name.append(robot)