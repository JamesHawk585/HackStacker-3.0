from flask import make_response, jsonify, request, session, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from flask_migrate import Migrate
# import ipdb
import datetime 
# from marshmallow_sqlalchemy import SQLAlchemySchema
from schema import blog_post_schema
from schema import blog_posts_schema

from config import app, db, api, ma
from models import User, BlogPost, Comment, Category, db
from sqlalchemy.exc import IntegrityError
# from marshmallow import fields



@app.route('/blog_posts', methods=['GET', 'POST'])
def blog_posts():
    if request.method == 'GET':

        blog_posts = BlogPost.query.all()

        response = make_response(
            blog_posts_schema.dump(blog_posts),
            200
        )
        return response
    
    elif request.method == 'POST':
        json_dict = request.get_json()

        blog_post = BlogPost(
            title = json_dict['title'],
            blog_content = json_dict['blog_content'],

        )

        # unknown function: now() is an issue in the migration.  
        # Always downgrade migrations prior to making changes directly to a migrations file. 
        # Add Tom Tobar to Linkedin. 
        
        db.session.add(blog_post)
        db.session.commit()

        response = make_response(
            blog_post_schema.dump(blog_post),
            201
        )

        return response



# form data object

@app.route('/blog_posts/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def blog_post_by_id(id):
    blog_post = BlogPost.query.filter_by(id=id).first()

    if request.method == 'GET':

        return make_response(
            blog_post_schema.dump(blog_post),
            200
        )

    elif request.method == 'PATCH':
        for attr in request.get_json():
            setattr(blog_post, attr, request.get_json()[attr])

            db.session.add(blog_post)
            db.session.commit()


            response = make_response(
                blog_post_schema.dump(blog_post),
                200
            )

            return response 

    elif request.method == 'DELETE': 
        db.session.delete(blog_post) 
        db.session.commit()


        response = make_response(
            blog_post_schema.dump(blog_post),
            200
        )

        return response 