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
from api.iam import Signup
from api.iam import CheckSession
from api.iam import Login
from api.iam import Logout



class UserSchema(ma.SQLAlchemySchema):
    id = fields.Int(dump_only=True)

    class Meta:
        model = User
    username = ma.auto_field()
    bio = ma.auto_field()
    blog_posts = ma.auto_field()
    comments = ma.auto_field()


    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "user_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class BlogPostSchema(ma.SQLAlchemySchema):
        id = fields.Int(dump_only=True)
    
        class Meta:
            model = BlogPost
    
        title = ma.auto_field()
        blog_content = ma.auto_field()
        publication_date = ma.auto_field()
        edited_at = ma.auto_field()
        user_id = ma.auto_field()
    
        url = ma.Hyperlinks(
            {
                "self": ma.URLFor(
                    "blog_post_by_id",
                    values=dict(id="<id>")),
                "collection": ma.URLFor("blog_posts"),
            }
        )

blog_post_schema = BlogPostSchema()
blog_posts_schema = BlogPostSchema(many=True)

class CommentSchema(ma.SQLAlchemySchema):
    id = fields.Int(dump_only=True)
        
    class Meta:
        model = Comment
        
    comment_content = ma.auto_field()
        
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "comment_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("comments"),
        }
    )

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

class CategorySchema(ma.SQLAlchemySchema):
    id = fields.Int(dump_only=True)
            
    class Meta:
        model = Category
            
    name = ma.auto_field()
    description = ma.auto_field()
            
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "category_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("categories"),
        }
    )

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)