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

from schema import comments_schema
from schema import comment_schema


@app.route('/comment/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def comment_by_id(id):
    comment = Comment.query.filter_by(id=id).first()

    if request.method == 'GET':

        return make_response(
            comment_schema.dump(comment),
            200
        )
    
    
    elif request.method == 'PATCH':
        for attr in request.get_json():
            setattr(comment, attr, request.get_json()[attr])

            db.session.add(comment)
            db.session.commit()

            # ipdb.set_trace()
            return make_response(
                comments_schema.dump(comment),
                200
            ) 
        
    elif request.method == 'DELETE':
        db.session.delete(comment)
        db.session.commit()


        response = make_response(
            comments_schema.dump(comment),
            200
        )

        return response 

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        comments = Comment.query.all()

        return make_response(
            comments_schema.dump(comments),
            200
        )

    elif request.method == 'POST':
        json_dict = request.get_json()
        comment = Comment(
            comment_content = json_dict['comment_content'],
        )

        db.session.add(comment)
        db.session.commit()


        return make_response(
            comments_schema.dump(comment),
            201
        )

