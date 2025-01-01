
from models import db, PetSitter
from app import app
# from faker import Faker


pet_sitters = [
    PetSitter(sitter_name='John Doe', location='123 Main St, Baton Rouge, LA, 70801', price=55),
    PetSitter(sitter_name='Jane Smith', location='456 Elm St, Baton Rouge, LA, 70802', price=60),
    PetSitter(sitter_name='Jim Brown', location='789 Oak St, Baton Rouge, LA, 70803', price=65),
    PetSitter(sitter_name='Mary Green', location='101 Pine St, Baton Rouge, LA, 70804', price=50),
    PetSitter(sitter_name='Tom White', location='202 Cedar St, Baton Rouge, LA, 70805', price=55),
    PetSitter(sitter_name='Emily Black', location='303 Birch St, Baton Rouge, LA, 70806', price=60),
    PetSitter(sitter_name='Chris Blue', location='404 Maple St, Baton Rouge, LA, 70807', price=65),
    PetSitter(sitter_name='Patricia Red', location='505 Ash St, Baton Rouge, LA, 70808', price=70),
    PetSitter(sitter_name='Michael Yellow', location='606 Redwood St, Baton Rouge, LA, 70809', price=55),
    PetSitter(sitter_name='Linda Purple', location='707 Pinecone St, Baton Rouge, LA, 70810', price=60),
]

with app.app_context():
    db.session.query(PetSitter).delete()  # This deletes all pet sitters in the table
    db.session.commit()
    for sitter in pet_sitters:
        db.session.add(sitter)
    db.session.commit()
    for sitter in PetSitter.query.all():
        print(sitter.sitter_name, sitter.location, sitter.price)

        

# fake = Faker()

# def generate_baton_rouge_address():
#     street = fake.street_address()
#     city = 'Baton Rouge'
#     state = 'LA'
#     zip_code = fake.zipcode_in_state('LA')

#     return f'{street}, {city}, {state}, {zip_code}'


# pet_sitters = [PetSitter(
#     sitter_name = fake.name(),
#     location = generate_baton_rouge_address(),
#     price = fake.random_int(min=50, max=70)
# )for _ in range(10)
# ]
  
# with app.app_context():
#     # db.drop_all()
#     # db.session.commit()
#     # db.create_all()
#     # db.session.commit()
#     PetSitter.query.delete()
#     db.session.commit()
#     for sitter in pet_sitters:
#         db.session.add(sitter)
#     db.session.commit()
#     for sitter in pet_sitters:
#         print(sitter.sitter_name, sitter.location, sitter.price)
