# app.py

from flask import Flask, request, jsonify
import logging

from flask_migrate import Migrate
from models import db, bcrypt, PetOwner, PetSitter , Appointment
from datetime import date

from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
# CORS(app)
# CORS(app, origins=["http://localhost:3000"])  

# CORS(app)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)  


@app.route("/")
def home():
    return "Welcome to the Pet Sitter app!"


@app.route('/signup', methods=['POST'])
def post():
    try:
        data = request.get_json()
        # logging.debug(f"Received data: {data}")  # Log the received data
        
       
        user_name = data.get('user_name')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        pet_name = data.get('pet_name')
        pet_type = data.get('pet_type')
        zip_code = data.get('zip_code')

        if password != confirm_password:
            return jsonify({'error': 'Password do not match'}), 400
               
        if not all([user_name, password, confirm_password, pet_name, pet_type, zip_code]):
            return jsonify({'error': 'All fields are required.'}), 400
        
        if PetOwner.query.filter(PetOwner.user_name==user_name).first():
            return jsonify({'error': 'Username already exists. Please choose another one.'}), 400
        new_pet_owner = PetOwner(
            user_name=user_name,
            password=password,
            pet_name=pet_name,
            pet_type=pet_type,
            zip_code=zip_code
        )
        db.session.add(new_pet_owner)  
        db.session.commit()  
        return jsonify(new_pet_owner.to_dict()), 201
    except Exception as e:
        logging.error(f"An error occurred during signup: {str(e)}")  # Log the exception
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@app.route('/pet_sitters', methods=['GET'])
def get():
    pet_sitters = PetSitter.query.all()
    
    return jsonify([sitter.to_dict() for sitter in pet_sitters])

@app.route('/pet_sitters/<int:id>', methods=['GET'])
def get_pet_sitter(id):
    pet_sitter = PetSitter.query.filter(PetSitter.id==id).first()
    sitter_data = pet_sitter.to_dict()
    sitter_data['avg_rating'] = pet_sitter.avg_rating()
    return jsonify(sitter_data)

@app.route('/appointment', methods=['POST'])

def appointment_form():
    data = request.get_json()
    pet_name = data.get('pet_name')
    pet_type = data.get('pet_type')
    date = data.get('date')
    duration = data.get('duration')

    if not isinstance(pet_name, str):
        raise ValueError('Pet name must be string.')
    if not pet_type or not isinstance(pet_type, str):
        raise ValueError('Pet type is required and must be string.')
    if not date or not isinstance(date, date):
        raise ValueError('Date is required and must be type date.')
    if not duration or not isinstance(duration, int):
        raise ValueError('Duration is required and must be type integer.')

    new_appointment = Appointment(
        pet_name = pet_name,
        pet_type = pet_type,
        date = date,
        duration = duration
    )
    db.session.add(new_appointment)
    db.session.commit()

    return jsonify(new_appointment.to_dict()), 201

@app.route('/appointment/<int:id>', methods=['POST'])

def rate_service(id):
    data = request.get_json()
    rating = data.get('rating')
    if rating is not None:
        if rating < 1 or rating > 5 or not isinstance(rating, int):
            return jsonify({'error': 'Rating must be between 1 and 5 and must be integer.'}), 400    
        rate_service = Appointment.query.filter(Appointment.id==id).first()

        if not rate_service:
            return jsonify({'error': 'Appointment not found'}), 404
        rate_service.rating = rating

        db.session.commit()
        return jsonify({'message': 'Rating submitted successfully.'}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
