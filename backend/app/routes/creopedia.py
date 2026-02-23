from flask import Blueprint, request, jsonify
from app import db
from app.models.creature import Creature
from app.models.creopedia_progress import CreopediaProgress
from app.models.island import Island
from app.utils.auth_middleware import token_required
import datetime

creopedia_bp = Blueprint('creopedia', __name__)

@creopedia_bp.route('/creatures', methods=['GET'])
@token_required
def get_creatures(current_user):
    island = Island.query.filter_by(user_id=current_user.id).first()
    if not island:
        return jsonify({'error': 'Île introuvable'}), 404

    creatures = Creature.query.all()
    progress_list = CreopediaProgress.query.filter_by(island_id=island.id).all()
    collected_ids = {p.creature_id for p in progress_list if p.collected}

    result = [c.to_dict(collected=(c.id in collected_ids)) for c in creatures]
    total = len(result)
    collected = len(collected_ids)

    return jsonify({
        'creatures': result,
        'stats': {
            'total': total,
            'collected': collected,
            'percentage': round((collected / total * 100), 1) if total > 0 else 0
        }
    }), 200

@creopedia_bp.route('/toggle', methods=['POST'])
@token_required
def toggle_creature(current_user):
    data = request.get_json()
    creature_id = data.get('creature_id')
    collected = data.get('collected', True)

    island = Island.query.filter_by(user_id=current_user.id).first()
    if not island:
        return jsonify({'error': 'Île introuvable'}), 404

    progress = CreopediaProgress.query.filter_by(
        island_id=island.id,
        creature_id=creature_id
    ).first()

    if progress:
        progress.collected = collected
        progress.collected_date = datetime.datetime.utcnow() if collected else None
    else:
        progress = CreopediaProgress(
            island_id=island.id,
            creature_id=creature_id,
            collected=collected,
            collected_date=datetime.datetime.utcnow() if collected else None
        )
        db.session.add(progress)

    db.session.commit()
    return jsonify({'success': True, 'creature_id': creature_id, 'collected': collected}), 200
