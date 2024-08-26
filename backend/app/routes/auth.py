# app/routes/auth.py
from flask import Blueprint, request, jsonify
from app.models.doctor import Doctor
from app import db

bp = Blueprint('auth', __name__)  # Changed from auth_bp to bp

@bp.route('/register/doctor', methods=['POST'])  # Changed from auth_bp to bp
def register_doctor():
    data = request.json
    new_doctor = Doctor(name=data['name'], email=data['email'], specialty=data['specialty'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"message": "Doctor registered successfully"}), 201