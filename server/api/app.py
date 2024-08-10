from flask import make_response, jsonify, request, session, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from flask_migrate import Migrate
import datetime 
# from marshmallow_sqlalchemy import SQLAlchemySchema

from config import app, db, api, ma
from models import User, BlogPost, Comment, Category, db
from sqlalchemy.exc import IntegrityError
# from marshmallow import fields


from api.user import users, user_by_id
from api.blog_post import blog_posts, blog_post_by_id
from api.category import categories, category_by_id
from api.comment import comments, comment_by_id
from api.cookie import cookies
from api.iam import Signup, CheckSession, Login, Logout
from api.schema import UserSchema, BlogPostSchema, CommentSchema, CategorySchema
from api.schema import users, user_by_id







