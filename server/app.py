# app.py

from flask import Flask

from flask_migrate import Migrate
from models import db, PetOwner  

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)  
db.init_app(app)

@app.route("/")
def home():
    return "Welcome to the Pet Sitter app!"

if __name__ == "__main__":
    app.run(debug=True)
