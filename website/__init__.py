'''
makes website folder a python package
means that we can import website folder and run init.py file
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #__name__ is name of file that you ran
    app.config['SECRET_KEY'] = 'random string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #stores db inside website folder
    db.init_app(app) #tells db what app were gonna use

    #need to tell init.py about our routes

    from .views import views
    from .auth import auth

    '''
    define these as empty routes because anything inside views and auth files starts with the url_prefix (es) define below 
    '''
    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/')

    from . import models

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    