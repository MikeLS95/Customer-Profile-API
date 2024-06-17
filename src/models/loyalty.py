from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from init import db, ma

class Loyalty(db.Model):
    __tablename__ = "loyalties"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id'))
    points: Mapped[int] = mapped_column()
    rewards: Mapped[str] = mapped_column(String(300))


class TravelGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'group_id', 'points', 'rewards')