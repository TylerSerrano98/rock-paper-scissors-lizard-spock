from players import Players
from human import Human
from ai import AI

class game:
    def __init__(self):
        pass

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def single_player(self):
      while True:
          response = input("/n How many players? (1 or 2)")
          if int(response) == 1:
              self.player_two == AI()
              break
          elif int (response)==2:
              self.multi_player == Human()

    def single_player_gesture(self):
        self.single_player.show_gesture_options()
        self.single_player.choose_player_gesture()




    def multi_player(self):
        pass