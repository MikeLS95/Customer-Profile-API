from marshmallow import ValidationError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.passports_bp import passport_bp
from blueprints.loyalties_bp import loyalties_bp
from blueprints.groups_bp import groups_bp


app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(passport_bp)
app.register_blueprint(loyalties_bp)
app.register_blueprint(groups_bp)


@app.route('/')
def index():
    return 'Customer Travel Profile API.'


@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'ERROR': 'Not found'}, 404


@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'ERROR': vars(err)["messages"]}, 400


@app.errorhandler(KeyError)
def missing_key(err):
    return {'ERROR': f"Missing field: {str(err)}"}, 400


print(app.url_map)
