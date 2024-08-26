# app/routes/auth.py
from flask import Blueprint, request, jsonify
from app.models.doctor import Doctor
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register/doctor', methods=['POST'])
def register_doctor():
    data = request.json
    new_doctor = Doctor(name=data['name'], email=data['email'], specialty=data['specialty'])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"message": "Doctor registered successfully"}), 201