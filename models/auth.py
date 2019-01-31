from gino_db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    phone = db.Column(db.String)

    def __repr__(self):
        return "User model"
