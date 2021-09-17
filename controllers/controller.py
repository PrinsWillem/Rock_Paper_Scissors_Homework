from models.player_list import add_new_player
from werkzeug.wrappers import request
from app import app
from flask import render_template, request
from models.player import Player
from models.player_list import attendees_info, add_new_player
from models.game import Game

@app.route("players")
def add_player():
    player_name = request.form["player"]
    player_choice = request.form["choice"]
    new_player = Player(player_name, player_choice)
    add_new_player(new_player)
    return render_template("index.html", title="My Game", attendees_info=attendees_info)