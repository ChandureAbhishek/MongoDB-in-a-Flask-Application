from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://abhishekchandure:Ganu9823418815@first-sample-cluster.notyr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client.flask_db


def create_app():
    app = Flask(__name__)
    # from .view import view
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    return app



