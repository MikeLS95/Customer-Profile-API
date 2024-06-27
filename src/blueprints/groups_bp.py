from flask import Blueprint, request
from init import db
from models.group import Group, GroupSchema
from models.user import User
from auth import admin


groups_bp = Blueprint('groups', __name__, url_prefix='/groups')


@groups_bp.route('/', methods=['GET'])
@admin
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
@admin
def one_group(id):
    group = db.get_or_404(Group, id)
    return GroupSchema(
        exclude=[
            "first_member_id",
            "second_member_id",
            "third_member_id",
            "fourth_member_id"
        ]).dump(group)


@groups_bp.route('/', methods=['POST'])
@admin
def add_group():
    params = GroupSchema().load(request.json)
    stmt = db.select(Group).where(Group.name == params["name"])
    name_match = db.session.scalar(stmt)

    # Checks to see if group name in database, if is, returns error message
    if name_match:
        return {'ERROR': 'Group name already exists, please choose a unique name.'}, 400

    errors = validate_user_ids(params)
    if errors:
        return {'ERROR': errors}, 400

    # requirements for new group, third and fourth member optional
    group = Group(
        name=params["name"],
        first_member_id=params["first_member_id"],
        second_member_id=params["second_member_id"],
        third_member_id=params["third_member_id"],
        fourth_member_id=params["fourth_member_id"]
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


# function for retrieving all group member user_ids
def validate_user_ids(params):
    errors = []
    user_ids = [
        params["first_member_id"], params["second_member_id"],
        params.get("third_member_id"), params.get("fourth_member_id")
    ]

    # Check if the user_id provided matches one on database, if not, returns error message
    for user_id in user_ids:
        if user_id is not None:  # Check for optional third and fourth members
            user = User.query.get(user_id)
            if not user:
                errors.append(f"User with ID {user_id} does not exist."), 400

    return errors if errors else None


@groups_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@admin
def update_group(id):
    group = db.get_or_404(Group, id)
    params = GroupSchema().load(request.json, partial=True, unknown='exclude')

    # required parameters for updating group
    group.name = params.get('name', group.name)
    group.first_member_id = params.get(
        'first_member_id', group.first_member_id)
    group.second_member_id = params.get(
        'second_member_id', group.second_member_id)
    group.third_member_id = params.get(
        'third_member_id', group.third_member_id)
    group.fourth_member_id = params.get(
        'fourth_member_id', group.fourth_member_id)

    db.session.commit()
    return GroupSchema(
        exclude=[
            "first_member_id",
            "second_member_id",
            "third_member_id",
            "fourth_member_id"
        ]).dump(group), 200


@groups_bp.route('/<int:id>', methods=['DELETE'])
@admin
def delete_group(id):
    group = db.get_or_404(Group, id)
    db.session.delete(group)
    db.session.commit()
    return ({'message': 'Group deleted'}), 200
