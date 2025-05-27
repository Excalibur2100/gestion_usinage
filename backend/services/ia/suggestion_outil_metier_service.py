from sqlalchemy.orm import Session
from datetime import datetime
from random import uniform
from db.schemas.ia.suggestion_outil_metier_schemas import SuggestionOutilIARequest
from db.models.tables.ia.suggestion_outil import SuggestionOutil

def generer_suggestion_outil_ia(data: SuggestionOutilIARequest, db: Session) -> dict:
    # Simulation IA : score et choix aléatoire
    outil_id = 1  # à remplacer par moteur IA réel
    score = round(uniform(0.70, 0.95), 2)

    suggestion = SuggestionOutil(
        piece_id=data.piece_id,
        outil_id=outil_id,
        score=score,
        commentaire=f"Suggestion IA pour {data.operation or 'opération inconnue'}",
        date_suggestion=datetime.utcnow()
    )

    db.add(suggestion)
    db.commit()
    db.refresh(suggestion)

    return {
        "suggestion_id": suggestion.id,
        "piece_id": suggestion.piece_id,
        "outil_id": suggestion.outil_id,
        "score": suggestion.score,
        "commentaire": suggestion.commentaire
    }