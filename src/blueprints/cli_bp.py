from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.group import Group
from models.loyalty import Loyalty
from models.passport import Passport


db_commands = Blueprint('db', __name__)


# Command used for replacing the database with the seeded entity data below in the database
@db_commands.cli.command('create')
def db_create():
    # Deletes current data in database
    db.drop_all()
    # Inserts new data in database
    db.create_all()
    print('Created tables')


    # Seeds users in the database
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
            password=bcrypt.generate_password_hash('test123').decode('utf-8'),
        )
    ]
    
    db.session.add_all(users)
    db.session.commit()


    # Seeds passports in the database
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


    # Seeds loyalties in the database
    loyalties = [
        Loyalty(
            supplier="QANTAS",
            type="airline",
            user_id=2
        ),
        Loyalty(
            supplier="hurts",
            type="car",
            user_id=2
        )
    ]

    db.session.add_all(loyalties)
    db.session.commit()


    # Seeds groups in the database
    groups = [
        Group(
            name="Group 1",
            first_member_id=2,
            second_member_id=4
        ),
        Group(
            name="Group 2",
            first_member_id=3,
            second_member_id=2
        )
    ]

    db.session.add_all(groups)
    db.session.commit()
    print('Database seeded')