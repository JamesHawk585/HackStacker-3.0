from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from config import db, bcrypt
from models.user import User
from models.blog_post import BlogPost
from models.category import Category
from models.comment import Comment

join_table = db.Table('blog_post_to_category',
                      db.Column("blog_post_id", db.Integer, db.ForeignKey("blog_post.id")),
                      db.Column("category_id", db.Integer, db.ForeignKey("category.id")),
                      )