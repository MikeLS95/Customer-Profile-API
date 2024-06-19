from flask import Blueprint, request
from init import db
from models.passport import Passport, PassportSchema
from models.user import User


# TO be done -----
# - Make sure when passport is retrieved, added or updated that user first and last names appear in json.


passport_bp = Blueprint('passport', __name__, url_prefix='/passport')


# Create a new passport if a user exists and doesn't already have a passport associated with their user_id
@passport_bp.route('/', methods=['POST'])
#admin only
def add_passport():
    params = PassportSchema().load(request.json)
    stmt = db.select(Passport).where(Passport.user_id == params['user_id'])
    pass_match = db.session.scalar(stmt)
    # Displays error if user_id already has a passport_id
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
    user_exists = User.query.get(params['user_id'])
    # makes sure the user exists
    if not user_exists:
        return {'ERROR': 'user_id does not exist'}, 404
    db.session.add(passport)
    db.session.commit()
    return PassportSchema().dump(passport), 201


# Retrieves all passports in database, shows user_id
@passport_bp.route('/', methods=['GET'])
# admin only
def all_passports():
    stmt = db.select(Passport)
    passports = db.session.scalars(stmt).all()
    return PassportSchema(many=True).dump(passports)


# Retrieve a passport from the provided passport id
@passport_bp.route('/<int:id>', methods=['GET'])
# admin only
def one_passport(id):
    passport = db.get_or_404(Passport, id)
    return PassportSchema().dump(passport)


# Retrieve and update a passport form the selected passport id
@passport_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# admin only
def update_passport(id):
    passport = db.get_or_404(Passport, id)
    params = PassportSchema().load(request.json, partial=True, unknown='exclude')
    # Required parameters for updating
    passport.issue_country = params.get('issue_country', passport.issue_country)
    passport.birth_country = params.get('birth_country', passport.birth_country)
    passport.passport_number = params.get('passport_number', passport.passport_number)
    passport.issue_date = params.get('issue_date', passport.issue_date)
    passport.expiration_date = params.get('expiration_date', passport.expiration_date)
    db.session.commit()
    return PassportSchema().dump(passport)


# Retrieve and delete a passport from the selected passport id
@passport_bp.route('/<int:id>', methods=['DELETE'])
# admin only
def delete_passport(id):
    passport = db.get_or_404(Passport, id)
    db.session.delete(passport)
    db.session.commit()
    return {}