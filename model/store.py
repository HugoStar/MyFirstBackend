from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True) # noqa
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name: str) -> None:
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'items': [item.json() for item in self.items.all()],
        }

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> 'StoreModel':
        store = StoreModel.query.filter_by(name=name).first()
        return store
