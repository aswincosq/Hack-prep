from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app,resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, world!")

if __name__=="__main__":
    app.run(debug=True)