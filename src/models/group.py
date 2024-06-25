from marshmallow import fields
from init import db, ma
from models.user import UserSchema


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='groups')


class GroupSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name', 'email'])

    class Meta:
        fields = ('id', 'name', 'user')