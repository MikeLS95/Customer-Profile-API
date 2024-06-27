from marshmallow import fields
from init import db, ma


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    first_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    second_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    third_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    fourth_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    first_member = db.relationship('User', foreign_keys=[first_member_id], back_populates='first_member')
    second_member = db.relationship('User', foreign_keys=[second_member_id], back_populates='second_member')
    third_member = db.relationship('User', foreign_keys=[third_member_id], back_populates='third_member')
    fourth_member = db.relationship('User', foreign_keys=[fourth_member_id], back_populates='fourth_member')
    

class GroupSchema(ma.Schema):
    first_member_id = fields.Integer(allow_none=True)
    second_member_id = fields.Integer(allow_none=True)
    third_member_id = fields.Integer(allow_none=True, missing=None)
    fourth_member_id = fields.Integer(allow_none=True, missing=None)
    first_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'])
    second_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'])
    third_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'], allow_none=True)
    fourth_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'], allow_none=True)

    class Meta:
        fields = ('id', 'name', 'first_member_id', 'second_member_id', 'third_member_id', 'fourth_member_id', 'first_member', 'second_member', 'third_member', 'fourth_member')