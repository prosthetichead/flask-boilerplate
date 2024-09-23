from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 

    # Import and register blueprints
    from .routes.main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app