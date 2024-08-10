from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from config import db, bcrypt


class BlogPost(db.Model):

    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    blog_content = db.Column(db.String(5000))
    publication_date = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())
    blog_card_thumbnail = db.Column(db.String)
    blog_card_banner = db.Column(db.String)
    
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    @validates('title', 'blog_content')
    def validate_length(self, key, string):
        if ( key == 'blog_content'):
            if len(string) >= 5000:
                raise ValueError("Blog posts must be 5000 characters or less.")
            if ( key == 'title'):
                raise ValueError('Title must be 50 characters or less.')
        return string 