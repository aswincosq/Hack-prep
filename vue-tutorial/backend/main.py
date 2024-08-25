from flask_cors import CORS
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':"*"}})

@app.route('/shark', methods=['GET'])
def shark():
    return ("Hello, this is a freaking good shark")

Games = [
    {
        'id' : uuid.uuid4().hex,
        'title':'GTA V',
        'genre':'action-adventure',
        'played':True,
    },
    {
        'id' : uuid.uuid4().hex,
        'title':'the last of us',
        'genre':'survival',
        'played':False,
    },
    {
        'id' : uuid.uuid4().hex,
        'title':'RDR 2',
        'genre':'action-adventure',
        'played':True,
    },
    {
        'id' : uuid.uuid4().hex,
        'title':'Batman:Arkham Knight',
        'genre':'fighting',
        'played':True,
    },
    {
        'id' : uuid.uuid4().hex,
        'title':'God of War:Ragnarok',
        'genre':'hack-and-slash',
        'played':False,
    },
    {
        'id' : uuid.uuid4().hex,
        'title':'Spider-Man',
        'genre':'Sci-Fi',
        'played':False,
    }
]

@app.route('/games', methods=['GET','POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        Games.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] = 'Game Added !'
    else:
        response_object['games'] = Games
    return jsonify(response_object)


@app.route('/games/<game_id>', methods=['PUT'])
def single_game(game_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        Games.append({
            'id' : game_id,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] = 'Game Updated !'
    else:
        response_object['games'] = Games
    return jsonify(response_object)

def remove_game(game_id):
    for game in Games:
        if game.get('id')==game_id:
            Games.remove(game)
            return True
    return False


if __name__=="__main__":
    app.run(debug=True)