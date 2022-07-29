from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
#script_dir = os.path.dirname(__file__)
#db = SQLAlchemy(app)


from app import routes
