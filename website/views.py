from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user #can access anything from user model as current user if user is logged in
from . import models
from . import db
import json

'''
defines url endpoints for front end of site
define that this file is a blueprint for our app
don't need to define all routes in one file
'''

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST']) #decorator
@login_required
def home(): #route
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = models.Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteId']
    note = models.Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})