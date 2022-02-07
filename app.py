from datetime import timedelta

from db import db

from flask import Flask

from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.debug = True

api = Api(app)


@app.route('/')
def index() -> None:
    return 'Hello my backend server'


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)
