# backend/tests/test_models/achat/test_lignes_reception.py

import pytest
from backend.db.models.tables.achat.lignes_reception import LigneReception
from backend.db.models.tables.achat.receptions import Reception
from sqlalchemy.orm import Session


def test_create_ligne_reception(db_session: Session):
    reception = Reception(
        numero_reception="REC-TEST-999",
        commande_id=1,
        statut="en_attente",
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()
    db_session.refresh(reception)

    ligne = LigneReception(
        reception_id=reception.id,
        designation="Vis M10",
        quantite_commandee=100.0,
        quantite_recue=90.0
    )
    db_session.add(ligne)
    db_session.commit()
    db_session.refresh(ligne)

    assert ligne.id is not None
    assert getattr(ligne, "designation") == "Vis M10"
    assert getattr(ligne, "quantite_commandee") == 100.0
    assert getattr(ligne, "quantite_recue") == 90.0
    assert getattr(ligne, "reception_id") == getattr(reception, "id")
    assert repr(ligne) == (
        f"<LigneReception(id={ligne.id}, designation='Vis M10', "
        f"commandée=100.0, reçue=90.0)>"
    )