# models.py


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class PetOwner(db.Model):
    __tablename__ = 'pet_owners'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pet {self.username}>'
