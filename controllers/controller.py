from werkzeug.wrappers import request
from app import app
from flask import render_template, request
from models.player import Player
from models.game import Game
import random

@app.route('/')
def welcome():
    return render_template("welcome.html", title="Home")

@app.route('/game-player')
def index():
    return render_template("player1.html", title="player1_choice")

@app.route('/<choice_1>')
def player_choice_vs_player(choice_1):
    return render_template("player2.html", title="player2_choice", choice_1=choice_1)

@app.route('/<choice_1>/<choice_2>')
def play_the_game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game()
    winner = game.play(player_1, player_2)
    return render_template("result.html", winner = winner)

@app.route('/game-computer')
def player_choice_vs_computer():
    return render_template("player_vs_com.html", title="player1_choice")

@app.route('/game-computer/<choice>')
def play_the_game_vs_computer(choice):
    player = Player("Player", choice)
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    computer = Player("Computer", computer_choice)
    game = Game()
    winner = game.play(player, computer)
    return render_template("result.html", winner = winner)




    
