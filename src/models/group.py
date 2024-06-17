from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from init import db, ma

class Group(db.Model):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(300))


class TravelGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id')