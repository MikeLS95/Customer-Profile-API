from flask import Blueprint, request
from init import db
from models.loyalty import Loyalty, LoyaltySchema
from models.user import User
from auth import admin


loyalties_bp = Blueprint('loyalties', __name__, url_prefix='/loyalties')


@loyalties_bp.route('/', methods=['GET'])
def all_loyalties():
    stmt = db.select(Loyalty)
    loyalties = db.session.scalars(stmt).all()
    return LoyaltySchema(many=True).dump(loyalties)


# Using a specific loyalty ID, retrieves specified loyalty, 404 if no ID matches
@loyalties_bp.route('/<int:id>', methods=['GET'])
def one_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    return LoyaltySchema().dump(loyalty)


@loyalties_bp.route('/', methods=['POST'])
@admin
def add_loyalty():
    params = LoyaltySchema().load(request.json)

    # Requirements for a new loyalty
    loyalty = Loyalty(
        supplier=params["supplier"],
        type=params["type"],
        user_id=params["user_id"],
    )

    # Error message for if no user id matching query
    user_exists = User.query.get(params['user_id'])
    if not user_exists:
        return {'ERROR': 'user_id does not exist'}, 404

    # Adds and commits the new loyalty to the database
    db.session.add(loyalty)
    db.session.commit()
    return LoyaltySchema().dump(loyalty), 201


# Retrieves specified loyalty ID and updates, 404 if no ID matches
@loyalties_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@admin
def update_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    params = LoyaltySchema().load(request.json, partial=True, unknown='exclude')

    loyalty.supplier = params.get('supplier', loyalty.supplier)
    loyalty.type = params.get('type', loyalty.type)

    db.session.commit()
    return LoyaltySchema().dump(loyalty), 200


# Retrieves specified loyalty ID and deletes, 404 of no ID matches
@loyalties_bp.route('/<int:id>', methods=['DELETE'])
@admin
def delete_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    db.session.delete(loyalty)
    db.session.commit()
    return ({'message': 'Loyalty deleted'}), 200
