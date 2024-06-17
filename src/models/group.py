from init import db, ma

class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)

    # users_id = db.Column(db.String, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='groups', cascade='all, delete')


class TravelGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')