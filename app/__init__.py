from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.auth import auth
    from app.main import main

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main)
    
    return app