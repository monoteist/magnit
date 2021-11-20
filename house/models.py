from house import db


class House(db.Model):
    __tablename__ = 'houses'
    house_id = db.Column(db.Integer(), primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    family_count = db.Column(db.Integer(), nullable=False)

    def __repr__(self) -> str:
        return f'Дом № {self.house_id}'