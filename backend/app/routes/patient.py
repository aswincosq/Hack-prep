# app/routes/patient.py
from flask import Blueprint, request, jsonify
from app.models import Patient
from app import db

bp = Blueprint('patient', __name__)

@bp.route('/register', methods=['POST'])
def register_patient():
    data = request.json
    new_patient = Patient(
        full_name=data['full_name'],
        email=data['email'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        primary_phone=data['primary_phone']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient registered successfully"}), 201

# Add more patient-related routes as needed