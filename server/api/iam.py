from flask import make_response, jsonify, request, session, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from flask_migrate import Migrate
import ipdb
import datetime 
from marshmallow_sqlalchemy import SQLAlchemySchema

from config import app, db, api, ma
from models import User, BlogPost, Comment, Category, db
from sqlalchemy.exc import IntegrityError
from marshmallow import fields


class Signup(Resource):
    def post(self):

        # password validations 

        request_json = request.get_json()

        username=request_json['username']
        password=request_json['password']
        bio=request_json['bio']

        user = User(
            username=username,
            bio=bio
        )
        # ipdb.set_trace()
        user.password_hash = password

        try: 
            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id
            return user.to_dict(), 201
            
        
        except IntegrityError: 

            return {'error': "422 Unprocessable Entity"}, 422

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict(), 200
        return {'error': '401 Unauthorized'}, 401

class Login(Resource):
    def post(self):

        request_json = request.get_json()

        username = request_json['username']
        password = request_json['password']


        user = User.query.filter(User.username == username). first()

        if user: 
            if user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
            return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204
        return {'error': '401 Unauthorized'}, 401

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Signup, '/CheckSession', endpoint='check_session')
api.add_resource(Signup, '/login', endpoint='login')
api.add_resource(Signup, '/logout', endpoint='logout')

def expiration_date(delay):
    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=delay)
    return expire_date