# app/routes/prescription.py
from flask import Blueprint, request, jsonify
from app.models import Prescription
from app import db

bp = Blueprint('prescription', __name__)

@bp.route('/create', methods=['POST'])
def create_prescription():
    data = request.json
    new_prescription = Prescription(
        appointment_id=data['appointment_id'],
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        medication=data['medication'],
        dosage=data['dosage'],
        frequency=data['frequency'],
        duration=data['duration'],
        notes=data.get('notes', '')
    )
    db.session.add(new_prescription)
    db.session.commit()
    return jsonify({"message": "Prescription created successfully"}), 201

# Add more prescription-related routes as needed