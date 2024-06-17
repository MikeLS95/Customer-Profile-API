from datetime import timedelta
from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from models.user import User, UserSchema

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/login', methods=['POST'])
def login():
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {'token': token}