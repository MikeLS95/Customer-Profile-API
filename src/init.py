from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

# Gets JWT_KEY from .env file
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
# Gets URI from .env file
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
# Shows returned json response as entered in schema
app.json.sort_keys = False

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
