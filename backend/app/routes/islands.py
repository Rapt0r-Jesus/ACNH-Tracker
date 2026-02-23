L'erreur est claire : le fichier islands.py existe mais il est vide ou n'a pas le islands_bp défini. Il faut créer le contenu de tous les fichiers routes. Voici ce qu'il faut mettre dans chacun :
backend/app/routes/islands.py
pythonfrom flask import Blueprint, request, jsonify
from app import db
from app.models.island import Island
from app.utils.auth_middleware import token_required

islands_bp = Blueprint('islands', __name__)

@islands_bp.route('', methods=['POST'])
@token_required
def create_island(current_user):
    data = request.get_json()
    name = data.get('name', '').strip()
    hemisphere = data.get('hemisphere', '')

    if not name or not hemisphere:
        return jsonify({'error': 'Nom et hémisphère requis'}), 400
    if hemisphere not in ['north', 'south']:
        return jsonify({'error': 'Hémisphère invalide'}), 400

    island = Island(user_id=current_user.id, name=name, hemisphere=hemisphere)
    db.session.add(island)
    db.session.commit()
    return jsonify(island.to_dict()), 201

@islands_bp.route('', methods=['GET'])
@token_required
def get_islands(current_user):
    islands = Island.query.filter_by(user_id=current_user.id).all()
    return jsonify([i.to_dict() for i in islands]), 200
