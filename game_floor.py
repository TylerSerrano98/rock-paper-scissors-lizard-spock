from players import Players
from human import Human
from ai import AI

class game:
    def __init__(self):
        self.player1 = Human(input('welcome player 1, Enter your name: '))
        self.player2 = AI()

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print('Welcome to rock, paper, scissors, lizard, spock the game is best of 3. Good luck!')
        print('Who beats who?:\n rock crushes scissors'
            '\n scissors cuts paper'
            '\n paper covers rock'
            '\n rock crushes lizard'
            '\n lizard poisons spock'
            '\n spock smashes scissors'
            '\n scissors decapitates lizard'
            '\n lizard eats paper'
            '\n paper disproves spock'
            '\n spock vaporizes rock')

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




   