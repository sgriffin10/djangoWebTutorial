from flask import Blueprint,render_template
from flask_login import login_required,current_user
'''
defines url endpoints for front end of site
define that this file is a blueprint for our app
don't need to define all routes in one file
'''

views = Blueprint('views',__name__)

@views.route('/') #decorator
@login_required
def home(): #route
    return render_template("home.html")
    # return "<h1>Test</h1>"