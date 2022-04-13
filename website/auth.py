from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from bson.objectid import ObjectId
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)
todos = db.todos

@auth.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('.index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)



@auth.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('.index'))