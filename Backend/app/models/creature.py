from app import db

class Creature(db.Model):
    __tablename__ = 'creatures'

    id = db.Column(db.Integer, primary_key=True)
    name_fr = db.Column(db.String(100), nullable=False)
    name_en = db.Column(db.String(100))
    category = db.Column(db.Enum('fish', 'bug', 'sea_creature', name='category_enum'), nullable=False)
    months_north = db.Column(db.JSON)   # ex: [1, 2, 3, 12]
    months_south = db.Column(db.JSON)
    hours_available = db.Column(db.String(100))
    location = db.Column(db.String(100))
    sell_price = db.Column(db.Integer)
    image_url = db.Column(db.String(255))

    def to_dict(self, collected=False):
        return {
            'id': self.id,
            'name_fr': self.name_fr,
            'name_en': self.name_en,
            'category': self.category,
            'months_north': self.months_north,
            'months_south': self.months_south,
            'hours_available': self.hours_available,
            'location': self.location,
            'sell_price': self.sell_price,
            'image_url': self.image_url,
            'collected': collected
        }
