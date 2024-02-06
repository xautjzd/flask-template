from flask import render_template

from flask_template.main import main_bp

@main_bp.route('/')
def index():
  return render_template('/index.html')

@main_bp.route('/post')
def posts():
  return render_template('/posts.html')
