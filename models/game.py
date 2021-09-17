from models.player import *

class Game:

    def __init__(self):
        pass

    def play(self, player1:Player, player2:Player):
    
        if player1.choice == player2.choice:
            return("it's a tie!")
        elif player1.choice == "Rock":
            if player2.choice == "Scissors":
                return player1
            else:
                return player2
        elif player1.choice == "Scissors":
            if player2.choice == "Paper":
                return player1
            else:
                return player2
        elif player1.choice == "Paper":
            if player2.choice == "Rock":
                return player1
            else:
                return player2
      
            