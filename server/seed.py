
# seed.py

import sys
import traceback
from random import choice
from faker import Faker
from models import PetOwner
from app import app
from models import db

if __name__ == '__main__':

    fake = Faker()
    with app.app_context():
        pets = ['cat', 'dog', 'bird']

        
        PetOwner.query.delete()
        db.session.commit()

        for _ in range(20):

            random_pet = choice(pets).lower()

            valid_zip = False
            while not valid_zip:
                    
                zip_code = fake.zipcode()
                try:
                    if random_pet not in pets:
                        raise ValueError(f'Invalid pet type: {random_pet}')
                    owner = PetOwner(
                        user_name = fake.user_name(),
                        password = fake.password(),
                        pet_name = fake.name(),
                        pet_type = random_pet,
                        zip_code = zip_code

                    )
                    
                    db.session.add(owner)
                    valid_zip = True
                except ValueError as e:
                    print(f'Invalid zip code. Try again: {e}')
                    pass
        db.session.commit()



