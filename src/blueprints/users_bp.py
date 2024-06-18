from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from models.user import User, UserSchema
from models.passport import Passport

users_bp = Blueprint('users', __name__, url_prefix='/users')


# Create a login key (C)
@users_bp.route('/login', methods=['POST'])
def login():
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {'token': token}
    else:
        return {'ERROR': 'Invalid email or password'}, 401
    

# Create User (C)
@users_bp.route('/', methods=['POST'])
def create_user():
    params = UserSchema().load(request.json, unknown='exclude')
    stmt = db.select(User).where(User.email == params['email'])
    user_match = db.session.scalar(stmt)
    if user_match:
        return {'ERROR': 'User already exists'}, 409
    user = User(
        email=params["email"],
        first_name=params["first_name"],
        last_name=params["last_name"],
        password=bcrypt.generate_password_hash(params["password"]).decode('utf-8'),
        is_admin=False,
    )
    db.session.add(user)
    db.session.commit()
    return UserSchema(exclude=['password']).dump(user), 201


# Read all users (R)
@users_bp.route('/', methods=['GET'])
# add admin only
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=["password"]).dump(users)


# Read one user (R)
@users_bp.route('/<int:id>', methods=['GET'])
# add admin only
def one_users(id):
    user = db.get_or_404(User, id)
    return UserSchema(exclude=["password"]).dump(user)


# Update user information (U)
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# User with ID or admin
def update_user(id):
    user = db.get_or_404(User, id)
    params = UserSchema().load(request.json, partial=True, unknown='exclude')
    user.email = params.get('email', user.email)
    user.first_name = params.get('first_name', user.first_name)
    user.last_name = params.get('last_name', user.last_name)
    user.is_admin = params.get('is_admin', user.is_admin)
    user.password = params.get('password', user.password)
    db.session.commit()
    return UserSchema(exclude=["password"]).dump(user)


# delete user (D) admin only
@users_bp.route('/<int:id>', methods=['DELETE'])
# add authentication, admin only
def delete_user(id):
    user = db.get_or_404(User, id)
    # add authorization
    db.session.delete(user)
    db.session.commit()
    return ({'message': 'User deleted'}), 200