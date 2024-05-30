from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Yo! Hello, World'

@main.route('/profile')
def profile():
    return 'Profile Page'