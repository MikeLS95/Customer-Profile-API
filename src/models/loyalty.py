from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Text
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma

class Loyalty(db.Model):
    __tablename__ = "Loyalties"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    points: Mapped[int] = mapped_column()
    rewards: Mapped[str] = mapped_column(Text)


class TravelGroupSchema(ma.Schema):
    password = fields.String(validate=Length(min=8, error='Password must be at least 8 characters long'), required=True)

    class Meta:
        fields = ('id', 'user_id', 'loyalty_id', 'password')