import logging

logger = logging.getLogger(__name__)

def calculer_parametres_usinage(piece, outils_disponibles=None, machines_disponibles=None):
    try:
        # Extraction des données de la pièce
        longueur = piece["longueur"]
        largeur = piece["largeur"]
        hauteur = piece["hauteur"]
        materiau = piece["materiau"]
        operations = piece["operations"]

        # Validation des données
        if longueur <= 0 or largeur <= 0 or hauteur <= 0:
            raise ValueError("Les dimensions doivent être positives.")
        if not isinstance(operations, list) or not operations:
            raise ValueError("La liste des opérations est invalide ou vide.")

        # Vérifie si les outils et machines sont fournis
        if outils_disponibles is None:
            outils_disponibles = []
        if machines_disponibles is None:
            machines_disponibles = []

        # Exemple : Vérifie si les outils nécessaires sont disponibles
        outils_requis = ["fraise", "foret"]  # Exemple d'outils nécessaires
        outils_manquants = [outil for outil in outils_requis if outil not in outils_disponibles]
        if outils_manquants:
            raise ValueError(f"Outils manquants : {', '.join(outils_manquants)}")

        # Exemple : Vérifie si une machine est disponible
        if "fraiseuse" not in machines_disponibles:
            raise ValueError("Aucune fraiseuse disponible pour cette opération.")

        # Calcul du brut nécessaire
        brut = {
            "longueur": longueur + 10,  # Ajout de surcote
            "largeur": largeur + 10,
            "hauteur": hauteur + 5
        }

        # Calcul des passes
        passes = calculer_passes(longueur, largeur, hauteur)

        # Calcul des vitesses de coupe (en fonction du matériau)
        vitesses_coupe = {
            "acier": 100,
            "aluminium": 300,
            "inox": 80
        }
        vitesse_coupe = vitesses_coupe.get(materiau.lower(), 50)  # Par défaut : 50 m/min

        # Calcul du temps d'usinage (simplifié)
        temps_usinage = (longueur * largeur * hauteur) / vitesse_coupe

        # Log des résultats
        logger.info("Calcul des paramètres d'usinage terminé avec succès.")

        return {
            "brut": brut,
            "passes": passes,
            "vitesse_coupe": vitesse_coupe,
            "temps_usinage": temps_usinage,
            "operations": operations
        }

    except KeyError as e:
        logger.error(f"Clé manquante dans les données : {e}")
        raise ValueError(f"Clé manquante dans les données : {e}")
    except Exception as e:
        logger.error(f"Erreur lors du calcul des paramètres : {e}")
        raise ValueError(f"Erreur lors du calcul des paramètres : {e}")


def calculer_passes(longueur, largeur, hauteur, tolerance=0.1):
    """
    Calcul du nombre de passes nécessaires pour l'ébauche et la finition.
    """
    passe_epaisseur = 5  # Épaisseur de matière enlevée par passe (mm)
    passes_ebauche = int(hauteur // passe_epaisseur)
    passe_finition = 1 if hauteur % passe_epaisseur <= tolerance else 2

    return {
        "ebauche": passes_ebauche,
        "finition": passe_finition
    }