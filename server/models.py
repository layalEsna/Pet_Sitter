# models.py


from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from uszipcode import SearchEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property



db = SQLAlchemy()
bcrypt = Bcrypt() 


class PetOwner(db.Model, SerializerMixin):
    __tablename__ = 'pet_owners'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    _hash_password = db.Column(db.String, nullable=False)
    pet_name = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)

    pet_sitters = db.relationship('PetSitter', secondary='appointments', back_populates='pet_owners')
    appointments = db.relationship('Appointment', back_populates='pet_owner', cascade='all, delete-orphan')

    serialize_only = ('id', 'user_name', 'pet_name', 'pet_type', 'zip_code')
    search_engine = SearchEngine(simple_zipcode=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        self._hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._hash_password, password)

    @validates('user_name')
    def user_name_validate(self, key, user_name):
        if not user_name or not isinstance(user_name, str):
            raise ValueError('user name is required and must be type of string.')
        return user_name
    
    @validates('pet_name')
    def pet_name_validate(self, key, pet_name):
        if not pet_name or not isinstance(pet_name, str):
            raise ValueError('Pet name is required and must be type of string.')
        return pet_name
    
    @validates('pet_type')
    def pet_type_validate(self, key, pet_type):
        valid_pets = ['cat', 'dog', 'bird']
        if not pet_type or not isinstance(pet_type, str):
            raise ValueError('Pet type is required and must be type of string.')
        if pet_type not in valid_pets:
            raise ValueError(f'Invalid pet type: {pet_type}. Must be one of {valid_pets}.')
        return pet_type
    
    @validates('zip_code')
    def zip_code_validate(self, key, zip_code):
        """
        Validates that the zip code:
        - Is a string of digits.
        - Has exactly 5 characters.
        - Exists in the real-world zip code database using the `uszipcode` library.
    
        Raises a ValueError if the zip code is invalid.
        """
        if not zip_code or not zip_code.isdigit() or len(zip_code) != 5:
            raise ValueError('Zip code must be a string of digits and must have 5 characters.')

        result = self.search_engine.by_zipcode(zip_code)
        if not result.zipcode:
            raise ValueError(f'Invalid zip code: {zip_code}')
        return zip_code

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'pet_name': self.pet_name,
            'pet_type': self.pet_type,
            'zip_code': self.zip_code
        }


    def __repr__(self):
        return f'<Pet {self.user_name}>'
    
class PetSitter(db.Model, SerializerMixin):
    __tablename__ = 'pet_sitters'

    id = db.Column(db.Integer, primary_key=True)
    sitter_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)


    pet_owners = db.relationship('PetOwner', secondary='appointments', back_populates='pet_sitters')
    appointments = db.relationship('Appointment', back_populates='pet_sitter', cascade='all, delete-orphan')

    serialize_only = ('id', 'sitter_name', 'location', 'price')


    @validates('sitter_name')
    def sitter_name_validate(self, key, sitter_name):
        if not sitter_name or not isinstance(sitter_name, str):
            raise ValueError('Pet sitter name is required and must be type of string.')
        if len (sitter_name) < 5:
            raise ValueError ('Pet Sitter name must be at least 5 characters.')
    
        return sitter_name
    @validates('location')
    def location_validate(self, key, location):
        if not location or not isinstance(location, str):
            raise ValueError ('Location is required and must be type of string.')
        if len (location) < 10:
            raise ValueError('Location must be at least 10 characters.')
        return location
    
    @validates('price')
    def price_validate(self, key, price):
        if not price or not isinstance(price, int):
            raise ValueError('Price is required and must be an integer')
        if price < 50 or price > 70:
            raise ValueError('Price must be between 50 and 70 inclusive.')
        return price
    
    def avg_rating(self):
        from sqlalchemy import func
        rating = db.session.query(func.avg(Appointment.rating)).filter(
            Appointment.pet_sitter_id == self.id).filter(Appointment.rating != None).scalar()
        return round(rating, 2) if rating else None


    

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True, default=None)
    status = db.Column(db.String, nullable=False)

    pet_owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.id'), nullable=False)
    pet_sitter_id = db.Column(db.Integer, db.ForeignKey('pet_sitters.id'), nullable=False)

    pet_owner = db.relationship('PetOwner', back_populates='appointments')
    pet_sitter = db.relationship('PetSitter', back_populates='appointments')

    serialize_only = ('id', 'date', 'duration', 'rating', 'status', 'pet_owner_id', 'pet_sitter_id')


    

