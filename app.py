from boggle import Boggle
from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()
board = boggle_game.make_board()

app = Flask(__name__)
app.config['SECRET_KEY'] = "wow-a-secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def boggle_start():
    """ home page with boggle board on it"""

    return render_template("home.html", board = board)

@app.route("/check", methods=['POST'])
def check_word():
    """ checks to see if the user provided a valid word that is also on the board"""

# On the server, take the form value and check if it is a valid word in the dictionary
# Next, make sure that the word is valid on the board using the check_valid_word function from the boggle.py file.
# Respond with JSON using the jsonify function from Flask ...
# Send a JSON response which contains either a dictionary of 
# {“result”: “ok”}, {“result”: “not-on-board”}, or {“result”: “not-a-word”}, so the front-end can provide slightly different messages depending if the word is valid or not.


# TO DO ... 
# TO DO ... 
# TO DO ... 

# Put the board in a session variable so we remember it
# Using jQuery, take the form value and using axios, make an AJAX request to send it to the server.

# On the front-end, display the response from the backend to notify the user if the word is valid and exists on the board, if the word is invalid, or if the word does not exist at all.
# The score for a word is equal to its length. If a valid word is guessed, add its score to the total and make sure to display the current score as it changes.
# You can store the score on the front-end for now: it does not need to persist.
# Instead of letting the user guess for an infinite amount of time, ensure that a game can only be played for 60 seconds. Once 60 seconds has passed, disable any future guesses.

# Now that you have a functional game, let’s keep track of how many times the user has played as well as their highest score so far. When the game ends, send an AJAX request to the server with the score you have stored on the front-end and increment the number of times you have played on the backend.

# Since you will be sending this data as JSON when you make an axios request, you will see this data come in your Flask app inside of request.json not request.form. Use pdb or IPython to set a breakpoint and see what request.json looks like, it is not the same data structure as request.form.

# Refactoring
# If you have not already, can you design your front-end in an Object Oriented way?
# Do your view functions have docstrings that describe what they are doing?
# Are you handling duplicate words? Make sure if you submit the same word, it does not count twice.