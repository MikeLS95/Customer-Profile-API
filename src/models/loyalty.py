from marshmallow import fields
from init import db, ma


class Loyalty(db.Model):
    __tablename__ = "loyalties"

    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='loyalties')


class LoyaltySchema(ma.Schema):
    # Nested users first and last names in passport json response
    user = fields.Nested('UserSchema', only=['first_name', 'last_name'])

    class Meta:
        fields = ('id', 'supplier', 'type', 'user_id', 'user')
