from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':"*"}})

@app.route('/shark', methods=['GET'])
def shark():
    return ("Hello, this is a freaking good shark")

Games = [
    {
        'title':'GTA V',
        'genre':'action-adventure',
        'played':True,
    },
    {
        'title':'the last of us',
        'genre':'survival',
        'played':False,
    },
    {
        'title':'RDR 2',
        'genre':'action-adventure',
        'played':True,
    },
    {
        'title':'Batman:Arkham Knight',
        'genre':'fighting',
        'played':True,
    },
    {
        'title':'God of War:Ragnarok',
        'genre':'hack-and-slash',
        'played':False,
    },
    {
        'title':'Spider-Man',
        'genre':'Sci-Fi',
        'played':False,
    }
]

@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'games': Games,
        'status': 'success'
    })

if __name__=="__main__":
    app.run(debug=True)