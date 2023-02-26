from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """general configuration"""
        
        # QUESTION: what does this do again?  
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_home(self):
        """testing the homepage to ensure the session variables are initializing correctly"""
        with app.test_client() as client:
                response = client.get("/")
                html = response.get_data(as_text = True)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(session.get('games-played'), 0)
                self.assertEqual(session.get('high-score'), 0)
                self.assertIn('current-board', session)

    def test_check(self):
        """testing the check functionality of the boggle game"""
        with app.test_client() as client:
             with client.session_transaction() as session:
                  session['current-board'] = [['T', 'K', 'I', 'X', 'B'],
                    ['G', 'R', 'W', 'H', 'A'],
                    ['S', 'U', 'P', 'M', 'T'],
                    ['S', 'H', 'C', 'C', 'F'],
                    ['L', 'I', 'F', 'I', 'V']]
        response = client.post('/check', json = {"word": "HAT"})
        self.assertEqual(response.json['result'], "ok")

    def test_newgame(self):
        """test the functionality of creating a new game"""
        with app.test_client() as client:
            with client.session_transaction() as session:
                   session['high-score'] = 10
                   session['games-played'] = 3
        response = client.post('/newgame', json = {"score": 5})
        self.assertEqual(response.json['highscore'], 10)
        self.assertEqual(response.json['games_played'], 4)
