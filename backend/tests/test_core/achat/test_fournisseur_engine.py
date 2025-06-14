import pytest
from backend.core.ia.fournisseur_engine import (
    generer_code_fournisseur_auto,
    detecter_type_metier_fournisseur,
    est_fournisseur_critique,
    detection_statut,
    suggestion_creation_fournisseur
)
from backend.db.schemas.achat.fournisseur_schemas import TypeFournisseur, StatutFournisseur


def test_generer_code_fournisseur_auto():
    code = generer_code_fournisseur_auto()
    assert code.startswith("FRN-")
    assert len(code) > 10
    assert code[4:].isdigit() is False  # le reste est une timestamp, pas un pur int


@pytest.mark.parametrize("description, attendu", [
    ("fourniture d'acier et inox", TypeFournisseur.fournisseur_matiere_premiere),
    ("vente d'outils coupants carbure", TypeFournisseur.fournisseur_outillage),
    ("centre d'usinage CNC", TypeFournisseur.machine_outil),
    ("traitement de surface et anodisation", TypeFournisseur.traitement_surface),
    ("service logistique et livraison", TypeFournisseur.transport),
    ("métrologie et inspection", TypeFournisseur.controle_qualite),
    ("logiciel FAO et ERP", TypeFournisseur.logiciel_support),
    ("atelier de fraisage", TypeFournisseur.sous_traitant_usinage),
    ("soudure MIG", TypeFournisseur.sous_traitant_soudure),
    ("gravure et marquage industriel", TypeFournisseur.peinture_industrielle),
    ("domaine non répertorié", TypeFournisseur.autre),
])
def test_detecter_type_metier_fournisseur(description, attendu):
    result = detecter_type_metier_fournisseur(description)
    assert result == attendu


@pytest.mark.parametrize("type_fournisseur, attendu", [
    (TypeFournisseur.fournisseur_acier, True),
    (TypeFournisseur.fournisseur_matiere_premiere, True),
    (TypeFournisseur.sous_traitant_usinage, True),
    (TypeFournisseur.traitement_thermique, True),
    (TypeFournisseur.logiciel_support, False),
    (TypeFournisseur.prestataire, False),
    (TypeFournisseur.fournisseur_generaliste, False),
])
def test_est_fournisseur_critique(type_fournisseur, attendu):
    assert est_fournisseur_critique(type_fournisseur) == attendu


@pytest.mark.parametrize("commentaire, attendu", [
    ("blacklisté pour fraude", StatutFournisseur.blacklisté),
    ("fermé en 2023", StatutFournisseur.inactif),
    ("bon fournisseur", StatutFournisseur.actif),
    ("", StatutFournisseur.actif),
    (None, StatutFournisseur.actif),
])
def test_detection_statut(commentaire, attendu):
    assert detection_statut(commentaire) == attendu


def test_suggestion_creation_fournisseur():
    fournisseur = suggestion_creation_fournisseur(
        nom="Fournisseur IA",
        description="usinage et fraisage de précision",
        email="ia@example.com",
        commentaire="Client stratégique",
        pays="France",
        adresse="1 rue IA",
        ville="Metz",
        code_postal="57000",
        telephone="0102030405",
        site_web="https://ai.com",
        contact_nom="Jean IA",
        contact_email="contact@ai.com",
        contact_telephone="0607080910"
    )

    assert fournisseur.nom == "Fournisseur IA"
    assert fournisseur.pays == "France"
    assert fournisseur.statut == StatutFournisseur.actif
    assert fournisseur.type == TypeFournisseur.sous_traitant_usinage
    assert fournisseur.code is not None
    assert fournisseur.code.startswith("FRN-")