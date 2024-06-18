from flask import Blueprint
from init import db, bcrypt
from models.user import User
# from models.group import Group
# from models.loyalty import Loyalty
from models.passport import Passport


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(
            email='admin@travelprofile.com',
            first_name='Admin',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        ),
        User(
            email='ben@travelprofile.com',
            first_name='Ben',
            last_name='Benson',
            password=bcrypt.generate_password_hash('benson123').decode('utf-8'),
        ),
        User(
            email='Margo@travelprofile.com',
            first_name='Margaret',
            last_name='Johnson',
            password=bcrypt.generate_password_hash('Maggie123').decode('utf-8'),
        ),
        User(
            email='GrahamB@travelprofile.com',
            first_name='Graham',
            last_name='Bert',
            password=bcrypt.generate_password_hash('benson123').decode('utf-8'),
        )
    ]
    
    db.session.add_all(users)
    db.session.commit()
    print('Users added')

    # groups = [
    #     Group(
    #         name='Group 1'
    #     )
    # ]

    # db.session.add_all(groups)
    # db.session.commit()
    # print('Groups added')

    # loyalties = [
    #     Loyalty(

    #     )
    # ]

    # db.session.add_all(loyalties)
    # db.session.commit()
    # print('Loyalties added')

    passports = [
        Passport(
            issue_country='Australia',
            birth_country='Australia',
            passport_number='PA453213',
            issue_date='2020-01-01',
            expiration_date='2030-01-01',
            user_id=2
        ),
        Passport(
            issue_country='Canada',
            birth_country='Australia',
            passport_number='CA467513',
            issue_date='2014-10-10',
            expiration_date='2024-10-10',
            user_id=3
        )
    ]

    db.session.add_all(passports)
    db.session.commit()
    print('Passports added')
         
