from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.routes import initialize_routes
# import logging


jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "secret_key"
    app.config["JWT_SECRET_KEY"] = "jwt_secret"
    # app.logger.setLevel(logging.DEBUG)

    jwt.init_app(app)

    # Initialize API routes
    api = Api(app)
    initialize_routes(api)

    return app
