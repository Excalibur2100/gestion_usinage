from datetime import datetime
from typing import Optional

from backend.db.schemas.achat.fournisseur_schemas import (
    TypeFournisseur,
    StatutFournisseur,
    FournisseurCreate
)


def generer_code_fournisseur_auto(prefix: str = "FRN") -> str:
    """
    Génère automatiquement un code fournisseur unique basé sur le timestamp UTC.
    """
    return f"{prefix}-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"


def detecter_type_metier_fournisseur(description: str) -> TypeFournisseur:
    """
    Détecte le type de fournisseur à partir d'une description ou d'un domaine d'activité.
    """
    desc = description.lower()

    if any(k in desc for k in ["acier", "barre", "profil", "tôle", "inox", "alu", "brut", "matière"]):
        return TypeFournisseur.fournisseur_matiere_premiere
    if any(k in desc for k in ["outil", "plaquette", "carbure", "foret", "fraise", "hss"]):
        return TypeFournisseur.fournisseur_outillage
    if any(k in desc for k in ["cnc", "machine-outil", "centre", "fraiseuse", "tour"]):
        return TypeFournisseur.machine_outil
    if any(k in desc for k in ["traitement", "thermique", "anodisation", "galvanisation", "surface"]):
        return TypeFournisseur.traitement_surface
    if any(k in desc for k in ["transport", "livraison", "logistique"]):
        return TypeFournisseur.transport
    if any(k in desc for k in ["métrologie", "contrôle", "certificat", "inspection"]):
        return TypeFournisseur.controle_qualite
    if any(k in desc for k in ["logiciel", "erp", "cao", "fao", "cam", "gestion"]):
        return TypeFournisseur.logiciel_support
    if any(k in desc for k in ["usinage", "décolletage", "fraisage", "tournage"]):
        return TypeFournisseur.sous_traitant_usinage
    if any(k in desc for k in ["soudure", "tig", "mig", "arc", "brasure"]):
        return TypeFournisseur.sous_traitant_soudure
    if any(k in desc for k in ["peinture", "revêtement", "marquage", "gravure"]):
        return TypeFournisseur.peinture_industrielle

    return TypeFournisseur.autre


def est_fournisseur_critique(type_fournisseur: TypeFournisseur) -> bool:
    """
    Indique si le type fournisseur est critique pour l’activité d’usinage/soudure.
    """
    critiques = {
        TypeFournisseur.fournisseur_matiere_premiere,
        TypeFournisseur.fournisseur_acier,
        TypeFournisseur.fournisseur_inox,
        TypeFournisseur.fournisseur_outillage,
        TypeFournisseur.outilleur,
        TypeFournisseur.machine_outil,
        TypeFournisseur.sous_traitant_usinage,
        TypeFournisseur.sous_traitant_fraisage,
        TypeFournisseur.sous_traitant_tournage,
        TypeFournisseur.traitement_thermique,
        TypeFournisseur.traitement_surface,
        TypeFournisseur.controle_qualite,
        TypeFournisseur.metrologie,
    }
    return type_fournisseur in critiques


def detection_statut(commentaire: Optional[str]) -> StatutFournisseur:
    """
    Déduit automatiquement le statut en fonction du commentaire.
    """
    if commentaire:
        lower = commentaire.lower()
        if "blacklist" in lower or "fraude" in lower:
            return StatutFournisseur.blacklisté
        if "inactif" in lower or "fermé" in lower:
            return StatutFournisseur.inactif
    return StatutFournisseur.actif


def suggestion_creation_fournisseur(
    nom: str,
    description: str,
    email: Optional[str] = None,
    commentaire: Optional[str] = None,
    pays: Optional[str] = "France",
    adresse: Optional[str] = None,
    ville: Optional[str] = None,
    code_postal: Optional[str] = None,
    telephone: Optional[str] = None,
    site_web: Optional[str] = None,
    contact_nom: Optional[str] = None,
    contact_email: Optional[str] = None,
    contact_telephone: Optional[str] = None
) -> FournisseurCreate:
    """
    Suggestion intelligente pour préremplir un fournisseur depuis une description métier.
    """
    return FournisseurCreate(
        nom=nom,
        email=email,
        pays=pays or "France",
        commentaire=commentaire,
        statut=detection_statut(commentaire),
        type=detecter_type_metier_fournisseur(description),
        code=generer_code_fournisseur_auto(),
        adresse=adresse,
        ville=ville,
        code_postal=code_postal,
        telephone=telephone,
        site_web=site_web,
        contact_nom=contact_nom,
        contact_email=contact_email,
        contact_telephone=contact_telephone
    )