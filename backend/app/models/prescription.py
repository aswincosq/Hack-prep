# app/models/prescription.py
from app import db
from datetime import datetime

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    prescription_date = db.Column(db.Date, default=datetime.utcnow().date())
    medication = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text)

    appointment = db.relationship('Appointment', backref='prescriptions')
    patient = db.relationship('Patient', backref='prescriptions')
    doctor = db.relationship('Doctor', backref='prescriptions')

    def __repr__(self):
        return f'<Prescription {self.id}: {self.patient.full_name} by Dr. {self.doctor.name}>'