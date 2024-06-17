from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from init import db, ma

class TravelGroup(db.Model):
    __tablename__ = "Travel Groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(300))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


class TravelGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id')