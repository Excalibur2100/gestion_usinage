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

    assert result["status"] == "success"
    assert result["data"]["brut"]["longueur"] == 110
    assert result["data"]["brut"]["largeur"] == 60
    assert result["data"]["brut"]["hauteur"] == 25
    assert result["data"]["passes"]["ebauche"] == 4
    assert result["data"]["passes"]["finition"] == 1
    assert result["data"]["vitesse_coupe"] == 100
    assert result["data"]["temps_usinage"] > 0

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

    with pytest.raises(ValueError, match="Aucune machine disponible pour cette opération."):
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