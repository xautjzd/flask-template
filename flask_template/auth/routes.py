from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from flask_template.auth import auth_bp

@auth_bp.route('/index')
def index():
  try:
    return render_template(f'/auth/index.html')
  except TemplateNotFound:
    abort(404)
