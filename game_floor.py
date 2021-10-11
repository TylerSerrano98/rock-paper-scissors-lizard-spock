from players import Players
from human import Human
from ai import AI

class game:
    def __init__(self):
        self.player1 = Human(input('welcome player 1, Enter your name: '))
        self.player2 = AI()

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def game_mode(self):
      while True:
          response = input("/n How many players? (1 or 2)")
          if int(response) == 1:
              self.player_two == AI()
              break
          elif int (response)==2:
              self.multi_player == Human()

    def player_one_gesture(self):
        self._player_one.show_gesture_options()
        self.player_one.choose_player_gesture()

    def player_two_gesture(self):
        self.player_two_.player_two_gesture()




   