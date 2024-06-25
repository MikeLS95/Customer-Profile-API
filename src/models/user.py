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

    passport = db.relationship('Passport', back_populates='user', cascade='all,delete')
    loyalties = db.relationship('Loyalty', back_populates='user', cascade='all,delete')
    groups = db.relationship('Group', back_populates='user', cascade='all,delete')


class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=6, max=22, error='Password must be at between 6 and 22 characters long.'), required=True)

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_admin')


