from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.DevelopmentConfig')
app.config.from_pyfile('config.py')

from project import routes
