from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, make_response, jsonify
from init import db
from models.user import User


def admin_only(fn):
    @jwt_required()
    def admin_check():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {'ERROR': 'You are do not have admin permissions'}, 403
        
    return admin_check


def authorize_owner(card):
    user_id = get_jwt_identity()
    if user_id != card.user_id and admin_only():
        abort(make_response(jsonify(error="You must be either the owner or an admin to access this resource")),403)