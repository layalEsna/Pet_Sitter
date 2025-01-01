# app.py

from flask import Flask, request, jsonify
import logging

from flask_migrate import Migrate
from models import db, bcrypt, PetOwner, PetSitter 

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

@app.route('/appointment')
def make_appointment():

    data = request.get_json()
    date = data.get('date')
    duration = data.get('duration')
    rating = data.get('data')




if __name__ == "__main__":
    app.run(debug=True, port=5000)
