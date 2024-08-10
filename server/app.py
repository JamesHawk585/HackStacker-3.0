from config import app, db, api 
from flask import Flask
from flask import send_from_directory 
from flask_restful import Resource 
from models.models import * 



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


from config import app, db, api 
from flask import Flask
from flask import send_from_directory 
from flask_restful import Resource 
from models.models import * 

class Index(Resource):
    """The first resource that a request is made to in production mode."""

    def get(self, orgId=None):
        """Renders the index.html document from the frontend.

        Args:
            orgId (int, optional): the organization id (mainly used for /my-organizations/:orgId). Defaults to None.

        Returns:
            Response: the index.html document.
        """
        # print(f"The CWD at index call is: {os.getcwd()}", flush=True)
        return send_from_directory("../client/dist", "index.html")