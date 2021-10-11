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

    def single_player(self):
        pass

    def multi_player(self):
        user_input = ("would you like to play multiplayer? yes or no:")
        if user_input == "yes":
            self.player2 = Human(input('welcome player 2, Enter your name: '))