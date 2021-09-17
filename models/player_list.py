from models.player import Player

names = []
choice = ["rock", "paper", "scissors"]

player_1 = Player(names[0], choice)
player_2 = Player(names[1], choice)

attendees_info = []

def add_new_player(player):
    attendees_info.append(player)