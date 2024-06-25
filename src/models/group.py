from marshmallow import fields
from init import db, ma


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    first_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    second_member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    first_member = db.relationship('User', foreign_keys=[first_member_id], back_populates='first_member')
    second_member = db.relationship('User', foreign_keys=[second_member_id], back_populates='second_member')


class GroupSchema(ma.Schema):
    first_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'])
    second_member = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'])

    class Meta:
        fields = ('id', 'name', 'first_member', 'second_member')