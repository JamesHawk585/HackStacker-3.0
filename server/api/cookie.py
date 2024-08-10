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

@app.route("/cookies", methods=['GET'])
def cookies():
    response = make_response({'message': "cookies route"}, 200)

    return response