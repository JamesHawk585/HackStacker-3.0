
from flask import make_response, jsonify, request, session, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from flask_migrate import Migrate
# import ipdb
import datetime 
# from marshmallow_sqlalchemy import SQLAlchemySchema

from config import app, db, api, ma
from models import User, BlogPost, Comment, Category, db
from sqlalchemy.exc import IntegrityError
# from marshmallow import fields

from schema import categories_schema
from schema import category_schema


@app.route('/categories', methods=['GET','POST'])
def categories():
    if request.method == 'GET':
        categories = Category.query.all()

        return make_response(
            categories_schema.dump(categories),
            200
        )

    elif request.method == 'POST':
        json_dict = request.get_json()
        category = Category(
            name = json_dict['name'],
            description = json_dict['description']
        )

        db.session.add(category)
        db.session.commit()

        return make_response(
            category_schema.dump(category),
            201
        )
    

@app.route('/category/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def category_by_id(id): 
    category = Category.query.filter_by(id=id).first()

    if request.method == 'GET':

        return make_response(
            category_schema.dump(category),
            200
        )
    
    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(category, attr, request.get_json(attr))

            db.session.add(category)
            db.session.commit()


            return make_response(
                category_schema.dump(category),
                200
            )
        
    elif request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()


        return make_response(
            category_schema.dump(category),
            200
        )