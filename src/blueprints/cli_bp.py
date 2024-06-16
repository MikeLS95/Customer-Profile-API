from flask import Blueprint
from init import db, bcrypt
from models.user import User


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(
            email='admin@travelprofile.com',
            first_name='Mike',
            last_name='Sheppard',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print('Users added')