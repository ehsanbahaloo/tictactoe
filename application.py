from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    
    if "board" not in session:
        session["board"] = [['', '', ''], ['', '', ''], ['', '', '']]
        session['turn'] = 'X'
    return render_template('game.html', game=session['board'], turn=session['turn'])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session['turn'] == 'X':
        session["turn"] = 'O'
    else:
        session['turn'] ='X'
    return redirect(url_for('index'))
