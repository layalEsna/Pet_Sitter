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

    # pet_sitters = db.relationship('PetSitter', secondary='appointments', back_populates='pet_owners')
    # appointments = db.relationship('Appointment', back_populates='pet_owner', cascade='all, delete-orphan')

    serialize_only = ('id', 'user_name', 'pet_name', 'pet_type', 'zip_code')
    search_engine = SearchEngine(simple_zipcode=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
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
