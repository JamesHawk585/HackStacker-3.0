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