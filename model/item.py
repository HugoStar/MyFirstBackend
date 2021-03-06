from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True) # noqa
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name: str, price: float, store_id: int) -> None:
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self) -> None:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'store_id': self.store_id,
            }

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> 'ItemModel':
        item = ItemModel.query.filter_by(name=name).first()
        return item
