from app import db
import datetime

class TurnipPrice(db.Model):
    __tablename__ = 'turnip_prices'

    id = db.Column(db.Integer, primary_key=True)
    island_id = db.Column(db.Integer, db.ForeignKey('islands.id'), nullable=False)
    week_start_date = db.Column(db.Date, nullable=False)
    purchase_price = db.Column(db.Integer, nullable=True)
    monday_am = db.Column(db.Integer, nullable=True)
    monday_pm = db.Column(db.Integer, nullable=True)
    tuesday_am = db.Column(db.Integer, nullable=True)
    tuesday_pm = db.Column(db.Integer, nullable=True)
    wednesday_am = db.Column(db.Integer, nullable=True)
    wednesday_pm = db.Column(db.Integer, nullable=True)
    thursday_am = db.Column(db.Integer, nullable=True)
    thursday_pm = db.Column(db.Integer, nullable=True)
    friday_am = db.Column(db.Integer, nullable=True)
    friday_pm = db.Column(db.Integer, nullable=True)
    saturday_am = db.Column(db.Integer, nullable=True)
    saturday_pm = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'island_id': self.island_id,
            'week_start_date': self.week_start_date.isoformat(),
            'purchase_price': self.purchase_price,
            'monday_am': self.monday_am, 'monday_pm': self.monday_pm,
            'tuesday_am': self.tuesday_am, 'tuesday_pm': self.tuesday_pm,
            'wednesday_am': self.wednesday_am, 'wednesday_pm': self.wednesday_pm,
            'thursday_am': self.thursday_am, 'thursday_pm': self.thursday_pm,
            'friday_am': self.friday_am, 'friday_pm': self.friday_pm,
            'saturday_am': self.saturday_am, 'saturday_pm': self.saturday_pm,
        }
