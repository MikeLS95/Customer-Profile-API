from flask import Blueprint, request
from init import db
from models.loyalty import Loyalty, LoyaltySchema
from models.user import User


loyalties_bp = Blueprint('loyalties', __name__, url_prefix='/loyalties')


@loyalties_bp.route('/', methods=['POST'])
def add_loyalty():
    params = LoyaltySchema().load(request.json)

    loyalty = Loyalty(
        supplier=params["supplier"],
        type=params["type"],
        user_id=params["user_id"],
    )
    
    # Error message for if no user id matching query
    user_exists = User.query.get(params['user_id'])
    if not user_exists:
        return {'ERROR': 'user_id does not exist'}, 404
    
    db.session.add(loyalty)
    db.session.commit()
    return LoyaltySchema().dump(loyalty), 201


@loyalties_bp.route('/', methods=['GET'])
def all_loyalties():
    stmt = db.select(Loyalty)
    loyalties = db.session.scalars(stmt).all()
    return LoyaltySchema(many=True).dump(loyalties)


@loyalties_bp.route('/<int:id>', methods=['GET'])
def one_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    return LoyaltySchema().dump(loyalty)


@loyalties_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    params = LoyaltySchema().load(request.json, partial=True, unknown='exclude')
    
    loyalty.supplier = params.get('supplier', loyalty.supplier)
    loyalty.type = params.get('type', loyalty.type)
    
    db.session.commit()
    return LoyaltySchema().dump(loyalty)


@loyalties_bp.route('/<int:id>', methods=['DELETE'])
def delete_loyalty(id):
    loyalty = db.get_or_404(Loyalty, id)
    db.session.delete(loyalty)
    db.session.commit()
    return ({'message': 'Loyalty deleted'}), 200