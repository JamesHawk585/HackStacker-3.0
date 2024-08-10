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
from schema import users_schema
from schema import user_schema



@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def user_by_id(id):
        user = User.query.filter_by(id=id).first()
        if request.method == 'GET':

    
            response = make_response(
                user_schema.dump(user),
                200
            )
            return response 
    
        elif request.method == 'PATCH':
            for attr in request.get_json():
                # ipdb.set_trace()
                setattr(user, attr, request.get_json()[attr])

                db.session.add(user)
                db.session.commit()
        
                return make_response(
                    user_schema.dump(user),
                    200
                )


        elif request.method == 'DELETE':
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()

            return make_response(
                user_schema.dump(user),
                200
            )


@app.route('/users', methods =['GET', 'POST'] )
def users():
    # ipdb.set_trace()
    if request.method == 'GET':

        users = User.query.all()

        response = make_response(
            users_schema.dump(users),
            200
        )
        return response 
    
    elif request.method == 'POST':
        json_dict = request.get_json()

        user = User(
            
            username = json_dict['username'],
            bio = json_dict['bio'],
        )

        db.session.add(user)
        db.session.commit()

        response = make_response(
            user_schema.dump(user),
            201
        )


        return response
