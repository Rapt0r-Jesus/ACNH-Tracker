from flask import Blueprint, request, jsonify
from app import db
from app.models.turnip_price import TurnipPrice
from app.models.island import Island
from app.utils.auth_middleware import token_required
import datetime

turnips_bp = Blueprint('turnips', __name__)

@turnips_bp.route('/prices', methods=['POST'])
@token_required
def save_prices(current_user):
    data = request.get_json()
    island = Island.query.filter_by(user_id=current_user.id).first()
    if not island:
        return jsonify({'error': 'Île introuvable'}), 404

    today = datetime.date.today()
    days_since_sunday = today.weekday() + 1 if today.weekday() != 6 else 0
    week_start = today - datetime.timedelta(days=days_since_sunday)

    price = TurnipPrice.query.filter_by(
        island_id=island.id,
        week_start_date=week_start
    ).first()

    if not price:
        price = TurnipPrice(island_id=island.id, week_start_date=week_start)
        db.session.add(price)

    fields = ['purchase_price', 'monday_am', 'monday_pm', 'tuesday_am', 'tuesday_pm',
              'wednesday_am', 'wednesday_pm', 'thursday_am', 'thursday_pm',
              'friday_am', 'friday_pm', 'saturday_am', 'saturday_pm']

    for field in fields:
        if field in data:
            setattr(price, field, data[field])

    db.session.commit()
    return jsonify(price.to_dict()), 201

@turnips_bp.route('/history', methods=['GET'])
@token_required
def get_history(current_user):
    island = Island.query.filter_by(user_id=current_user.id).first()
    if not island:
        return jsonify({'error': 'Île introuvable'}), 404

    limit = request.args.get('limit', 10, type=int)
    prices = TurnipPrice.query.filter_by(island_id=island.id)\
        .order_by(TurnipPrice.week_start_date.desc())\
        .limit(limit).all()

    return jsonify([p.to_dict() for p in prices]), 200
