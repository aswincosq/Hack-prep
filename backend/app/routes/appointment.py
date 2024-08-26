# app/routes/appointment.py
from flask import Blueprint, request, jsonify
from app.models import Appointment
from app import db

bp = Blueprint('appointment', __name__)

@bp.route('/create', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        appointment_type=data['appointment_type'],
        start_time=data['start_time'],
        end_time=data['end_time']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment created successfully"}), 201

# Add more appointment-related routes as needed