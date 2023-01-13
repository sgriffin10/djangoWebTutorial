'''
makes website folder a python package
means that we can import website folder and run init.py file
'''
from flask import Flask

def create_app():
    app = Flask(__name__) #__name__ is name of file that you ran
    app.config['SECRET_KEY'] = 'random string'

    return app
    
    