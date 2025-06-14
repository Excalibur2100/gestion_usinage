# backend/tests/test_core/achat/test_reception_engine.py

import pytest
from datetime import datetime
from sqlalchemy.orm import Session
from backend.core.ia.achat.reception_engine import (
    generer_numero_reception,
    suggestion_statut_par_conformite,
    generer_document_reception_placeholder
)
from backend.db.models.tables.achat.receptions import Reception


def test_generer_numero_reception(db_session: Session):
    # Insère une réception fictive pour simuler un enregistrement existant
    reception = Reception(
        numero_reception="REC-2025-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut="en_attente",
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()

    numero = generer_numero_reception(db_session)
    assert numero.startswith("REC-2025-")
    assert len(numero.split("-")) == 3


def test_suggestion_statut_par_conformite_complet():
    statut = suggestion_statut_par_conformite([10, 5], [10, 5])
    assert statut.value == "recue"


def test_suggestion_statut_par_conformite_partiel():
    statut = suggestion_statut_par_conformite([5, 0], [10, 10])
    assert statut.value == "partiellement_recue"


def test_suggestion_statut_par_conformite_attente():
    statut = suggestion_statut_par_conformite([0, 0], [10, 10])
    assert statut.value == "en_attente"


def test_suggestion_statut_par_conformite_erreur_longueurs():
    statut = suggestion_statut_par_conformite([10], [10, 10])
    assert statut.value == "en_attente"


def test_generer_document_reception_placeholder():
    path = generer_document_reception_placeholder(42)
    assert path.startswith("documents/receptions/reception_42_")
    assert path.endswith(".pdf")