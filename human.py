from players import Players

class Human(Players):
        def __init__(self, name):
            super().__init__(name)
            self.player1 = name
            self.player2 = name

        def gestures(self):
            self.gesture_select = input('Please enter: rock, paper, scissors, lizard, spock')
            if self.gesture_select in self.human_gestures:
                print(self.choice)
            else:
                while self.gesture_select not in self.human_gestures:
                    print('not a gesture.. Select: rock, paper, scissors, lizard, spock')
                    self.choice = input('Please enter: rock, paper, scissors, lizard, spock')

            print(f'gesture chosen: {self.gesture_select} ')