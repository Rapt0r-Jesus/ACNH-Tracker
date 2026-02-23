from app import db
import datetime

class CreopediaProgress(db.Model):
    __tablename__ = 'creopedia_progress'

    id = db.Column(db.Integer, primary_key=True)
    island_id = db.Column(db.Integer, db.ForeignKey('islands.id'), nullable=False)
    creature_id = db.Column(db.Integer, nullable=False)
    collected = db.Column(db.Boolean, default=False)
    collected_date = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint('island_id', 'creature_id', name='unique_island_creature'),
    )
