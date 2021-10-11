from players import Players
from human import Human
from ai import AI

class game:
    def __init__(self):
        self.player1 = Human(input('welcome player 1, Enter your name: '))
        self.player2 = AI()

    def run_game(self):
        self.display_welcome()
        self.game_mode()
        self.game_logic()
        self.game_winner()
        

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
              self.player2 == AI()
              break
          elif int (response)==2:
              self.player2 == Human()

    def game_logic(self):
        while (self.player1.score < 3 and self.player2.score < 3):
            self.player1.gestures()
            self.player2.gesture()
            
            if self.player1.human_gestures == self.player2.choice_gesture:
             print('tie, go again!')

            elif (self.player1.human_gestures == 'rock' and self.player2.choice_gesture == 'scissors') or \
                (self.player1.human_gestures == 'scissors' and self.player2.choice_gesture == 'paper') or \
                (self.player1.human_gestures == 'paper' and self.player2.choice_gesture == 'rock') or \
                (self.player1.human_gestures == 'rock' and self.player2.choice_gesture == 'lizard') or \
                (self.player1.human_gestures == 'lizard' and self.player2.choice_gesture == 'paper') or \
                (self.player1.human_gestures == 'spock' and self.player2.choice_gesture == 'scissors') or \
                (self.player1.human_gestures == 'lizard' and self.player2.choice_gesture == 'paper') or \
                (self.player1.human_gestures == 'paper' and self.player2.choice_gesture == 'spock') or \
                (self.player1.human_gestures == 'spock' and self.player2.choice_gesture == 'rock') or \
                (self.player1.human_gestures == 'scissors' and self.player2.choice_gesture == 'lizard'):

                self.player1.score += 1
                print(f'{self.player1.choice} beats {self.player2.choice_gesture} player 1 wins the round!')
                print(f'Current score Player 1: {self.player1.score} Player 2: {self.player2.score}')
                return self.game_logic()
            else:
                self.player2.score += 1
                print(f'{self.player2.choice_gesture} beats {self.player1.human_gestures} player 2 wins the round!')
                print(f'Current score Player 1: {self.player1.score} Player 2: {self.player2.score}')
        
   
   
    def game_winner(self):
        if self.player1.score == 3:
            print("f The winner is {self.player_one.name}!")
        elif self.player2.score == 3:
            print("f The winner is {self.player_two.name}!")


   
   
            

      
        



   