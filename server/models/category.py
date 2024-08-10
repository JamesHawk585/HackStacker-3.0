from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from config import db, bcrypt



class Category(db.Model):

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(50), unique=True)

    
    @validates(name, description)
    def validate_length(self, key, string):
        if ( key == 'name'):
            if len(string) >= 30:
                raise ValueError("Category name must be 80 characters or less.")
            if ( key == 'description'):
                raise ValueError('Category description must be 250 characters or less.')
        return string 

