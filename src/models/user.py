from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(100))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=8, error='Password must be at least 8 characters long.'), required=True)

    class Meta:
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_admin')


