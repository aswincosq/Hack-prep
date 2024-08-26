# app/models/doctor.py
from app import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    specialty = db.Column(db.String(100))
    # Add other fields as per your requirements

    def __repr__(self):
        return f'<Doctor {self.name}>'