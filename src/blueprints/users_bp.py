from flask import Blueprint
from flask import request
from init import db, bcrypt
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/login', methods=['POST'])
def login():
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')