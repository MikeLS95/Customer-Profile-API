from init import db, ma


class Passport(db.Model):
    __tablename__ = "passport"

    id = db.Column(db.Integer, primary_key=True)
    issue_country = db.Column(db.String, nullable=False)
    birth_country = db.Column(db.String, nullable=False)
    passport_number = db.Column(db.String, nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='passport')
                                                

class PassportSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'issue_country', 'birth_country', 'passport_number', 'issue_date', 'expiration_date')