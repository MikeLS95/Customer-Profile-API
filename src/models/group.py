from init import db, ma

class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)

    user_groups = db.Table('user-groups', 
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
    )


class GroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id')