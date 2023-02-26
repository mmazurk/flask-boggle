from boggle import Boggle
from flask import Flask, render_template, request, jsonify, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "wow-a-secret"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def boggle_start():
    """ home page with boggle board on it"""

    board = boggle_game.make_board()
    session['current-board'] = board

    if session.get('games-played') == None:
        session['games-played'] = 0
    
    if session.get('high-score') == None:
        session['high-score'] = 0
    
    highscore = session.get('high-score')
    games_played = session.get('games-played')

    return render_template("home.html", board = board, highscore = highscore, games_played = games_played)

@app.route("/check", methods=['POST'])
def check_word():
    """ checks to see if the user provided a valid word that is also on the board"""
    
    board = session['current-board']
    data = request.get_json()
    word_to_check = data['word'].strip().lower()
    result = boggle_game.check_valid_word(board, word_to_check)
    return jsonify({"result": result})

# to test if this is working in curl
# curl localhost:5000/check -d '{"word": "plant"}' -H 'Content-Type: application/json'

@app.route("/newgame", methods=['POST'])
def new_game():
    """ checks the high-score, incrememnts number of games played"""
    
    data = request.get_json()
    score = data['score']
    if score > session['high-score']:
        session['high-score'] = score

    games = session['games-played']
    games += 1
    session['games-played'] = games

    high_score = session["high-score"]
    games_played = session["games-played"]
 
    return jsonify({"highscore": high_score, "games_played": games_played})
