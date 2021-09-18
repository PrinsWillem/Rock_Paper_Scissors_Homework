from werkzeug.wrappers import request
from app import app
from flask import render_template, request
from models.player import Player
from models.game import Game
import random

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game()
    winner = game.play(player_1, player_2)
    return f"Player 1 chose: {player_1.choice}, Player 2 chose: {player_2.choice}. The winner is {winner}." 


@app.route('/<choice>')
def play_the_game_vs_computer(choice):
    player = Player("Player", choice)
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    computer = Player("Computer", computer_choice)
    game = Game()
    winner = game.play(player, computer)
    return f"Player chose: {player.choice}, Computer chose: {computer.choice}. The winner is {winner}"


    
