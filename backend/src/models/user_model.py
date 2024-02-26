from database.db import db
from app import app


class Users(db.Model):
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def add_user(cls, name):
        user = cls(name)
        db.session.add(user)
        db.session.commit()
        return user

    def to_dict(self):
        return {"id": self.id, "name": self.name, "created": self.created}


with app.app_context():
    db.create_all()
