from init import db, ma


class Loyalty(db.Model):
    __tablename__ = "loyalties"

    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='loyalties')


class LoyaltySchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'supplier', 'type')
