from flask import Blueprint
from init import db, bcrypt
from models.user import User
# from models.group import Group
# from models.loyalty import Loyalty
# from models.passport import Passport


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
        ),
        User(
            email='ben@travelprofile.com',
            first_name='Ben',
            last_name='Benson',
            password=bcrypt.generate_password_hash('benson123').decode('utf-8'),
        )
    ]
    
    db.session.add_all(users)
    db.session.commit()
    print('Users added')

    # groups = [
    #     Group(

    #     )
    # ]

    # db.session.add_all(group)
    # db.session.commit()
    # print('Groups added')

    # loyalties = [
    #     Loyalty(

    #     )
    # ]

    # db.session.add_all(loyalties)
    # db.session.commit()
    # print('Loyalties added')

    # passports = [
    #     Passport(

    #     )
    # ]

    # db.session.add_all(passports)
    # db.session.commit()
    # print('Passports added')
         
