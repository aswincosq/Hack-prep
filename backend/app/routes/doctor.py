from flask import Blueprint, request, jsonify,db
from werkzeug.security import generate_password_hash
import re

from backend.app.models.doctor import Doctor

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Validate phone number (simple example, adjust as needed)
    if not re.match(r"^\+?1?\d{9,15}$", data['phone']):
        return jsonify({"error": "Invalid phone number format"}), 400

    # Check if email or phone already exists
    if Doctor.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400
    if Doctor.query.filter_by(phone=data['phone']).first():
        return jsonify({"error": "Phone number already registered"}), 400

    new_doctor = Doctor(
        identifier=data['identifier'],
        name=data['name'],
        gender=data['gender'],
        profile_picture=data.get('profile_picture'),
        email=data['email'],
        phone=data['phone'],
        address_line=data['address_line'],
        city=data['city'],
        state=data['state'],
        country=data['country'],
        postal_code=data['postal_code'],
        description=data['description'],
        experience_years=data['experience_years'],
        qualifications=data['qualifications'],
        specialties=data['specialties'],
        password_hash=generate_password_hash(data['password'])
    )

    db.session.add(new_doctor)
    try:
        db.session.commit()
        return jsonify(new_doctor.to_fhir()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
