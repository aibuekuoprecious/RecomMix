# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import bp as routes_bp  # Update this line to use 'bp'

db = SQLAlchemy()

def create_app():
    # Create the Flask create_app instance
    app = Flask(__name__)

    # Configure my database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:new_password@34.224.63.159/RecomMix?auth_plugin=mysql_native_password'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)
    # Register my blueprints and other configurations here
    app.register_blueprint(routes_bp)  # Update this line to use 'routes_bp'

    return app
