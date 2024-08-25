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


@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])  # Added DELETE method
def single_game(game_id):
    response_object = {'status': 'success'}
    game_found = False  # Flag to check if game is found (New)

    if request.method == "PUT":
        post_data = request.get_json()
        for game in Games:  # Loop through games to find the correct one (Modified)
            if game['id'] == game_id:
                game['title'] = post_data.get('title')  # Directly update title (New)
                game['genre'] = post_data.get('genre')  # Directly update genre (New)
                game['played'] = post_data.get('played')  # Directly update played status (New)
                game_found = True
                response_object['message'] = 'Game Updated!'  # Updated message
                break
        if not game_found:  # Error handling for game not found (New)
            response_object = {'status': 'failure', 'message': 'Game not found!'}
            return jsonify(response_object), 404  # Return 404 if game not found (New)
    
    if request.method == "DELETE":  # New block to handle DELETE requests
        if remove_game(game_id):  # Use existing remove_game function
            response_object['message'] = 'Game Deleted!'  # New delete message
        else:
            response_object = {'status': 'failure', 'message': 'Game not found!'}  # Error handling for game not found
            return jsonify(response_object), 404  # Return 404 if game not found (New)
    
    return jsonify(response_object)  # Return response


def remove_game(game_id):
    for game in Games:
        if game.get('id')==game_id:
            Games.remove(game)
            return True
    return False


if __name__=="__main__":
    app.run(debug=True)