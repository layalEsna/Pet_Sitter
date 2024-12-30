
from models import db, PetSitter
from app import app
from faker import Faker

fake = Faker()

pet_sitters = [PetSitter(
    sitter_name = fake.name(),
    location = fake.address(),
    price = fake.random_int(min=50, max=70)
)for _ in range(20)
]
  
with app.app_context():
    for sitter in pet_sitters:
        db.session.add(sitter)
    db.session.commit()
    for sitter in pet_sitters:
        print(sitter.sitter_name, sitter.location, sitter.price)
