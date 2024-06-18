from flask import Blueprint, request
from init import db
from models.passport import Passport, PassportSchema

passport_bp = Blueprint('passport', __name__, url_prefix='/passport')

@passport_bp.route('/', methods=['POST'])
def add_passport():
    params = PassportSchema().load(request.json)
    stmt = db.select(Passport).where(Passport.user_id == params['user_id'])
    pass_match = db.session.scalar(stmt)
    if pass_match:
        return {'ERROR': 'Passport for selected user already exists'}, 409
    passport = Passport(
        issue_country=params["issue_country"],
        birth_country=params["birth_country"],
        passport_number=params["passport_number"],
        issue_date=params["issue_date"],
        expiration_date=params["expiration_date"],
        user_id=params["user_id"],
    )
    db.session.add(passport)
    db.session.commit()
    return PassportSchema().dump(passport), 201