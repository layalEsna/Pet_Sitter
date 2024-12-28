from app import app, db
from models import PetOwner

with app.app_context():
    # Query the PetOwner table
    pet_owner = PetOwner.query.all()
    print(pet_owner)
