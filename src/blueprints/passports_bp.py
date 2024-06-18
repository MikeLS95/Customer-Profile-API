from flask import Blueprint, request
from init import db
from models.passport import Passport, PassportSchema


# TO be done -----
# - Make sure when passport is retrieved, added or updated that user first and last names appear in json.


passport_bp = Blueprint('passport', __name__, url_prefix='/passport')

# Need to fix error where adding a new passport for a user that doesnt exists
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


@passport_bp.route('/', methods=['GET'])
# admin only
def all_passports():
    stmt = db.select(Passport)
    passports = db.session.scalars(stmt).all()
    return PassportSchema(many=True).dump(passports)


@passport_bp.route('/<int:id>', methods=['GET'])
# admin only
def one_passport(id):
    passport = db.get_or_404(Passport, id)
    return PassportSchema().dump(passport)


@passport_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
# admin only
def update_passport(id):
    passport = db.get_or_404(Passport, id)
    params = PassportSchema().load(request.json, partial=True, unknown='exclude')
    passport.issue_country = params.get('issue_country', passport.issue_country)
    passport.birth_country = params.get('birth_country', passport.birth_country)
    passport.passport_number = params.get('passport_number', passport.passport_number)
    passport.issue_date = params.get('issue_date', passport.issue_date)
    passport.expiration_date = params.get('expiration_date', passport.expiration_date)
    passport.user_id = params.get('user_id', passport.user_id)
    db.session.commit()
    return PassportSchema().dump(passport)