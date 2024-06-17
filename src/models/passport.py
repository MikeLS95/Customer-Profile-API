from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from init import db, ma


class Passport(db.Model):
    __tablename__ = "passport"
    # id: Mapped[int] = mapped_column(primary_key=True)
    # user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    # issue_country: Mapped[str] = mapped_column(String(30))
    # birth_country: Mapped[str] = mapped_column(String(30))
    # passport_number: Mapped[str] = mapped_column(String(15))
    # issue_date: Mapped[date] = mapped_column()
    # expiration_date: Mapped[date] = mapped_column()
    id = db.Column(db.Integer, primary_key=True)
    issue_country = db.Column(db.String, nullable=False)
    birth_country = db.Column(db.String, nullable=False)
    passport_number = db.Column(db.String, nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='passport')
                                                

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'issue_country', 'birth_country', 'passport_number', 'issue_date', 'expiration_date')