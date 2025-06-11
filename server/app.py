from flask import Flask
from flask_migrate import Migrate

from models import db,Student
# create flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initilize the db
db.init_app(app)

migration = Migrate(app, db)