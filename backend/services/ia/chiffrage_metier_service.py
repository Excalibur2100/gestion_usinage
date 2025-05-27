from sqlalchemy.orm import Session
from typing import Optional
from backend.core.ia.chiffrage_engine import ChiffrageEngine
from db.schemas.ia.chiffrage_metiers_schemas import ChiffrageSimpleRequest, ChiffrageCompletRequest, ChiffrageIntelligentRequest

def calculer_cout_total(data: ChiffrageSimpleRequest) -> float:
    return ChiffrageEngine.calculer_cout_total(data.cout_unitaire * data.temps_h, data.marge)

def chiffrage_complet(data: ChiffrageCompletRequest) -> dict:
    return ChiffrageEngine.calcul_complet(
        nb_operations=data.nb_operations,
        temps_moyen_op=data.temps_moyen_op,
        cout_horaire=data.cout_horaire,
        marge=data.marge,
        description=data.description
    )

def chiffrage_intelligent(data: ChiffrageIntelligentRequest, db: Session) -> dict:
    return ChiffrageEngine.chiffrage_complet(
        db=db,
        piece_id=data.piece_id,
        taux_marge=data.marge
    )