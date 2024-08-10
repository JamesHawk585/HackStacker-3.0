from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from config import db, bcrypt


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    bio = db.Column(db.String(250))
    profile_pic = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    blog_posts = db.relationship('BlogPost', backref='user')
    comments = db.relationship('Comment', backref='user')

    @validates('username')
    def validate_name(self, key, username):
        username_exists = db.session.query(User).filter(User.username==username).first()
        if not username:
            raise ValueError("username field is required")
        if username_exists:
            raise ValueError("username must be unique")
        elif key == 'username':
            if len(username) >= 80:
                raise ValueError("username must be 80 characters or less.")
        return username 

    @validates('bio')
    def validate_length(self, key, string):
        if len(string) > 250:
                raise ValueError('Bio must be 250 characters or less.')
        return string 

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.username}>'