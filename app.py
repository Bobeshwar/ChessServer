"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from moveEvaluator import evaluateScore
from flask import Flask,render_template,request
import chess

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

def makeMove(position):
    board = chess.Board(fen = position)
    moveGenerator = list(board.legal_moves)
    print(evaluateScore())
    move = moveGenerator[0]
    return move.uci();
@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/board')
def index():
    return render_template("index.html")


@app.route('/playermove', methods=["POST"])
def playermove():
    position = request.json["position"]
    move = makeMove(position)
    return {"move": move}
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
