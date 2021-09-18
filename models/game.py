from models.player import *

class Game:

    def __init__(self):
        pass

    def play(self, player1:Player, player2:Player):
    
        if player1.choice == player2.choice:
            return(None)
        elif player1.choice == "rock":
            if player2.choice == "scissors":
                return player1.name
            else:
                return player2.name
        elif player1.choice == "scissors":
            if player2.choice == "paper":
                return player1.name
            else:
                return player2.name
        elif player1.choice == "paper":
            if player2.choice == "rock":
                return player1.name
            else:
                return player2.name
      
            