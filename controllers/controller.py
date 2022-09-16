from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player
import random

@app.route('/index')
def show_index():
    return render_template('index.html')




@app.route('/result', methods=['POST'])
def call_result_of_game():
    player_1 = Player("Player 1", request.form['player_1_choice'])
    player_2 = Player("Player 2", request.form['player_2_choice'])

    this_game = Game(player_1, player_2)

    winner = this_game.who_wins()
    if winner is None:
        winning_message="it's a draw!"
    else:
        winning_message=winner.name + " wins!"

    # this_game = Game(player_1, player_2)
    # winner = this_game.who_wins()
    return render_template('result.html', title='Home', winning_message=winning_message, game=this_game)

    

@app.route('/<choice_1>/<choice_2>')
def result_of_game(choice_1, choice_2):

    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)

    this_game = Game(player_1, player_2)

    winner = this_game.who_wins()
    if winner is None:
        winning_message="it's a draw!"
    else:
        winning_message=winner.name + " wins!"

    # this_game = Game(player_1, player_2)
    # winner = this_game.who_wins()
    return render_template('result.html', title='Home', winning_message=winning_message, game=this_game)




@app.route('/result_against_computer', methods=['POST'])
def call_result_of_game_against_computer():
    # get random choice for computer to use
    list_of_choices =["rock", "paper", "scissors"]
    computer_choice = random.choice(list_of_choices)

    player = Player("Player", request.form['player_choice'])
    computer_player = Player("Computer", computer_choice)

    this_game = Game(player, computer_player)

    winner = this_game.who_wins()
    if winner is None:
        winning_message="it's a draw!"
    else:
        winning_message=winner.name + " wins!"

    return render_template('result.html', title='Home', winning_message=winning_message, game=this_game)

    