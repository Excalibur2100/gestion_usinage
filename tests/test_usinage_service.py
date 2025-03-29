import pytest
from services.usinage.usinage_service import calculer_parametres_usinage

def test_calcul_parametres_usinage_valide():
    piece = {
        "longueur": 100,
        "largeur": 50,
        "hauteur": 20,
        "materiau": "acier",
        "operations": ["fraisage", "perçage"]
    }
    outils_disponibles = ["fraise", "foret"]
    machines_disponibles = ["fraiseuse"]

    result = calculer_parametres_usinage(piece, outils_disponibles, machines_disponibles)

    assert result["brut"]["longueur"] == 110
    assert result["brut"]["largeur"] == 60
    assert result["brut"]["hauteur"] == 25
    assert result["passes"]["ebauche"] == 4
    assert result["passes"]["finition"] == 1
    assert result["vitesse_coupe"] == 100
    assert result["temps_usinage"] > 0

def test_calcul_parametres_usinage_outils_manquants():
    piece = {
        "longueur": 100,
        "largeur": 50,
        "hauteur": 20,
        "materiau": "acier",
        "operations": ["fraisage", "perçage"]
    }
    outils_disponibles = ["foret"]  # Manque "fraise"
    machines_disponibles = ["fraiseuse"]

    with pytest.raises(ValueError, match="Outils manquants : fraise"):
        calculer_parametres_usinage(piece, outils_disponibles, machines_disponibles)

def test_calcul_parametres_usinage_machine_absente():
    piece = {
        "longueur": 100,
        "largeur": 50,
        "hauteur": 20,
        "materiau": "acier",
        "operations": ["fraisage", "perçage"]
    }
    outils_disponibles = ["fraise", "foret"]
    machines_disponibles = []  # Pas de machine disponible

    with pytest.raises(ValueError, match="Aucune fraiseuse disponible pour cette opération."):
        calculer_parametres_usinage(piece, outils_disponibles, machines_disponibles)

def test_calcul_parametres_usinage_dimensions_invalides():
    piece = {
        "longueur": -100,  # Dimension invalide
        "largeur": 50,
        "hauteur": 20,
        "materiau": "acier",
        "operations": ["fraisage", "perçage"]
    }
    outils_disponibles = ["fraise", "foret"]
    machines_disponibles = ["fraiseuse"]

    with pytest.raises(ValueError, match="Les dimensions doivent être positives."):
        calculer_parametres_usinage(piece, outils_disponibles, machines_disponibles)