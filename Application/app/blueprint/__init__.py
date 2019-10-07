from flask import Blueprint
from flask_restful import Api

from app.controllers.test_controller import Test

blueprint  = Blueprint("api", __name__)
api = Api(blueprint)
api.add_resource(Test, '/', '/')