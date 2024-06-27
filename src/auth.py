from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from init import db
from models.user import User


# Function for ensuring user is_admin
def admin(fn):
    # ensures that the original functions metadata is preserved
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        @jwt_required()
        def checker():
            user_id = get_jwt_identity()
            stmt = db.select(User).where(User.id == user_id, User.is_admin)
            user = db.session.scalar(stmt)
            if user:
                return fn(*args, **kwargs)
            else:
                return {'ERROR': 'You are not an admin'}, 403

        return checker()

    return decorated_function
