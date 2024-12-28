# app.py

from flask import Flask, request

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length, EqualTo


from flask_migrate import Migrate
from models import db, bcrypt, PetOwner  

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)  


@app.route("/")
def home():
    return "Welcome to the Pet Sitter app!"

if __name__ == "__main__":
    app.run(debug=True)
