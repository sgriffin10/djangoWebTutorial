'''
makes website folder a python package
means that we can import website folder and run init.py file
'''
from flask import Flask

def create_app():
    app = Flask(__name__) #__name__ is name of file that you ran
    app.config['SECRET_KEY'] = 'random string'

    #need to tell init.py about our routes

    from .views import views
    from .auth import auth

    '''
    define these as empty routes because anything inside views and auth files starts with the url_prefix (es) define below 
    '''
    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/')

    return app

    