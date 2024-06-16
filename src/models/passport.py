from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma


class Passport(db.Model):
    __tablename__ = "passport"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    issue_country: Mapped[str] = mapped_column(String(30))
    birth_country: Mapped[str] = mapped_column(String(30))
    passport_number: Mapped[str] = mapped_column(String(15))
    issue_date: Mapped[date] = mapped_column(date)
    expiration_date: Mapped[date] = mapped_column(date)
                                                

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'issue_country', 'birth_country', 'passport_number', 'issue_date', 'expiration_date')