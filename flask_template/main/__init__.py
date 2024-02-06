from flask import Blueprint

main_bp = Blueprint('main', __name__)

from flask_template.main import routes
