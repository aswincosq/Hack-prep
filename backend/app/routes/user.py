from flask import Blueprint, request, jsonify
from ..models import User
from .. import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(email=data['email'], password=data['password'], user_type=data['user_type'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


