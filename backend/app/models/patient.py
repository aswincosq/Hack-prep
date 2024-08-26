# app/models/patient.py
from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    primary_phone = db.Column(db.String(20), nullable=False)
    profile_picture = db.Column(db.String(255))

    # Add any additional fields as per your requirements

    def __repr__(self):
        return f'<Patient {self.full_name}>'