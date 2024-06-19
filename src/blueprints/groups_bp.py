from flask import Blueprint
from init import db
from models.group import Group, GroupSchema


groups_bp = Blueprint('groups', __name__, url_prefix='/groups')


@groups_bp.route('/', methods=['GET'])
def all_groups():
    stmt = db.select(Group)
    groups = db.session.scalars(stmt).all()
    return GroupSchema(many=True).dump(groups)