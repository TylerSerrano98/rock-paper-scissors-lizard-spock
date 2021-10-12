from players import Players

class Human(Players):
        def __init__(self, name):
            super().__init__(name)
            self.name = name

        def gestures(self):
            self.choice_gesture = input('Please enter: rock, paper, scissors, lizard, spock')
            if self.choice_gesture in self.human_gestures:
                print(self.choice_gesture)
               
            else:
                 while self.choice_gesture not in self.human_gestures:
                    print('not a gesture.. Select: rock, paper, scissors, lizard, spock')
                    self.choice = input('Please enter: rock, paper, scissors, lizard, spock')
                     
            print(f'gesture chosen: {self.choice_gesture} ')