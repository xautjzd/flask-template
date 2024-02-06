import os
from flask import Flask
from dotenv import load_dotenv
import pymysql

from config import Config

from flask_template.extensions import db
from flask_template.main import main_bp 
from flask_template.auth import auth_bp

# Load envs configured in project .env file
load_dotenv()

# app must be initialized in __init__ file
app = Flask(__name__)

# Initialize Flask extensions here
# pymysql.install_as_MySQLdb()
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# db.init_app(app)

# Loaded db config info from Config class
app.config.from_object(Config)

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route('/test/')
def test_page():
  return '<h1>Testing the Flask Application Factory Pattern</h1>'
