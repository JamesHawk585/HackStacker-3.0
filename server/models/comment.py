from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from config import db, bcrypt

class Comment(db.Model):

    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(250))
    publication_date = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    @validates('comment_content')
    def validate_length(self, key, string):
        if len(string) >= 250:
            raise ValueError('Comments must be less than 250 characters in length')
        return string