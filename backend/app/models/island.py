from app import db

class Island(db.Model):
    __tablename__ = 'islands'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    hemisphere = db.Column(db.Enum('north', 'south', name='hemisphere_enum'), nullable=False)

    progress = db.relationship('CreopediaProgress', backref='island', lazy=True, cascade='all, delete-orphan')
    turnip_prices = db.relationship('TurnipPrice', backref='island', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'hemisphere': self.hemisphere
        }
