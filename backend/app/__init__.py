from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import User, Doctor, Patient, Appointment, Prescription

    from .routes import auth, doctor, patient, appointment, prescription,user
    app.register_blueprint(auth.bp)
    app.register_blueprint(doctor.bp)
    app.register_blueprint(patient.bp)
    app.register_blueprint(appointment.bp)
    app.register_blueprint(prescription.bp)


    @app.route('/')
    def hello_world():
        return 'Hello, Telemedicine!'

    return app
