from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(50), unique=True)
    active = db.Column(db.Boolean, default=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    profile_picture = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    address_line = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    description = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    qualifications = db.Column(db.Text)
    specialties = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_fhir(self):
        return {
            "resourceType": "Practitioner",
            "id": str(self.id),
            "identifier": [
                {
                    "system": "urn:oid:2.16.840.1.113883.4.6",
                    "value": self.identifier
                }
            ],
            "active": self.active,
            "name": [
                {
                    "use": "official",
                    "text": self.name
                }
            ],
            "gender": self.gender,
            "telecom": [
                {
                    "system": "email",
                    "value": self.email
                },
                {
                    "system": "phone",
                    "value": self.phone
                }
            ],
            "address": [
                {
                    "use": "work",
                    "line": [self.address_line],
                    "city": self.city,
                    "state": self.state,
                    "country": self.country,
                    "postalCode": self.postal_code
                }
            ],
            "qualification": [
                {
                    "code": {
                        "text": self.qualifications
                    }
                }
            ],
            "communication": [
                {
                    "text": self.specialties
                }
            ]
        }
