from flask import Blueprint, request
from init import db
from models.loyalty import Loyalty, LoyaltySchema
from models.user import User


loyalties_bp = Blueprint('loyalties', __name__, url_prefix='/loyalties')


@loyalties_bp.route('/', methods=['POST'])
def add_loyalty():
    params = LoyaltySchema().load(request.json)
    # stmt = db.select(Loyalty).where(Loyalty.user_id == params['user_id'])
    # loyalty_match = db.session.scalar(stmt)
    # if loyalty_match:
    #     return {'ERROR': 'Loyalty for selected user already exists'}, 409
    loyalty = Loyalty(
        supplier=params["supplier"],
        type=params["type"],
        user_id=params["user_id"],
    )
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