
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma

class TravelGroup(db.Model):
    __tablename__ = "Travel Groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(foreign_key=True)
    loyalty_id: Mapped[int] = mapped_column(foreign_key=True)
    password: Mapped[str] = mapped_column(String(200))


class TravelGroupSchema(ma.Schema):
    password = fields.String(validate=Length(min=6, error='Password must be at least 6 characters long'), required=True)

    class Meta:
        fields = ('id', 'user_id', 'loyalty_id', 'password')