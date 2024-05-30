from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return 'Sign up users'

@auth.route('/login')
def login():
    return 'Login users'

@auth.route('/logout')
def logout():
    return 'Logout users'