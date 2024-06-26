from typing import Optional
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, server_default='false')

    passports = db.relationship('Passport', back_populates='user', cascade='all,delete')
    loyalties = db.relationship('Loyalty', back_populates='user', cascade='all,delete')

    first_member = db.relationship('Group', foreign_keys='Group.first_member_id', back_populates='first_member', primaryjoin='User.id == Group.first_member_id', cascade='all,delete')
    second_member = db.relationship('Group', foreign_keys='Group.second_member_id', back_populates='second_member', primaryjoin='User.id == Group.second_member_id', cascade='all,delete')
    third_member = db.relationship('Group', foreign_keys='Group.third_member_id', back_populates='third_member', primaryjoin='User.id == Group.third_member_id', cascade='all,delete')
    fourth_member = db.relationship('Group', foreign_keys='Group.fourth_member_id', back_populates='fourth_member', primaryjoin='User.id == Group.fourth_member_id', cascade='all,delete')


class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=6, max=22, error='Password must be at between 6 and 22 characters long.'), required=True)
    last_name = fields.String(required=False)

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_admin')


