from flask import Blueprint, request
from init import db
from models.group import Group, GroupSchema
from models.user import User


groups_bp = Blueprint('groups', __name__, url_prefix='/groups')


@groups_bp.route('/', methods=['GET'])
def all_groups():
    stmt = db.select(Group)
    groups = db.session.scalars(stmt).all()
    return GroupSchema(
        many=True, 
        exclude=[
            "first_member_id", 
            "second_member_id",
            "third_member_id",
            "fourth_member_id"
            ]
    ).dump(groups)


# Using a specific loyalty ID, retrieves specified loyalty, 404 if no ID matches
@groups_bp.route('/<int:id>', methods=['GET'])
def one_group(id):
    group = db.get_or_404(Group, id)
    return GroupSchema().dump(group)


@groups_bp.route('/', methods=['POST'])
def add_group():
    params = GroupSchema().load(request.json)
    stmt = db.select(Group).where(Group.name == params["name"])
    name_match = db.session.scalar(stmt)
    if name_match:
        return {'ERROR': 'Group name already exists, please choose a unique name.'}, 400
    
    group = Group(
        name=params["name"],
        first_member_id=params["first_member_id"],
        second_member_id=params["second_member_id"]
    )

    db.session.add(group)
    db.session.commit()
    return GroupSchema(        
        exclude=[
            "first_member_id", 
            "second_member_id",
            "third_member_id",
            "fourth_member_id"
            ]).dump(group), 201