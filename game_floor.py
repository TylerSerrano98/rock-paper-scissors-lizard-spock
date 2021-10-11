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

    def game_logic(self):
        while (self.player1.score < 3 and self.player2.score < 3):
            self.player1.gestures()
            self.player2.gesture()
            
            if self.player1.choice == self.player2.choice:
             print('tie, go again!')

            elif (self.player1.choice == 'rock' and self.player2.choice == 'scissors') or \
                (self.player1.choice == 'scissors' and self.player2.choice == 'paper') or \
                (self.player1.choice == 'paper' and self.player2.choice == 'rock') or \
                (self.player1.choice == 'rock' and self.player2.choice == 'lizard') or \
                (self.player1.choice == 'lizard' and self.player2.choice == 'paper') or \
                (self.player1.choice == 'spock' and self.player2.choice == 'scissors') or \
                (self.player1.choice == 'lizard' and self.player2.choice == 'paper') or \
                (self.player1.choice == 'paper' and self.player2.choice == 'spock') or \
                (self.player1.choice == 'spock' and self.player2.choice == 'rock') or \
                (self.player1.choice == 'scissors' and self.player2.choice == 'lizard'):

                self.player1.score += 1
                print(f'{self.player1.choice} beats {self.player2.choice} player 1 wins the round!')
                print(f'Current score Player 1: {self.player1.score} Player 2: {self.player2.score}')
                return self.game_logic()
            else:
                self.player2.score += 1
                print(f'{self.player2.choice} beats {self.player1.choice} player 2 wins the round!')
                print(f'Current score Player 1: {self.player1.score} Player 2: {self.player2.score}')
        


   
   
   
   
    def game_winner(self):
        pass



   