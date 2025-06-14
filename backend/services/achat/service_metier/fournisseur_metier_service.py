from typing import Optional

from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    TypeFournisseur,
    StatutFournisseur
)


def verifier_domaine_usinage(type_fournisseur: TypeFournisseur) -> bool:
    """
    Vérifie si le fournisseur appartient au domaine de l'usinage, soudure ou services techniques associés.
    """
    domaines = [
        TypeFournisseur.fournisseur_matiere_premiere,
        TypeFournisseur.fournisseur_acier,
        TypeFournisseur.fournisseur_inox,
        TypeFournisseur.fournisseur_non_ferreux,
        TypeFournisseur.machine_outil,
        TypeFournisseur.fournisseur_outillage,
        TypeFournisseur.outilleur,
        TypeFournisseur.fournisseur_outils_de_mesure,
        TypeFournisseur.sous_traitant_usinage,
        TypeFournisseur.sous_traitant_tournage,
        TypeFournisseur.sous_traitant_fraisage,
        TypeFournisseur.sous_traitant_edm,
        TypeFournisseur.sous_traitant_soudure,
        TypeFournisseur.traitement_surface,
        TypeFournisseur.traitement_thermique,
        TypeFournisseur.peinture_industrielle,
        TypeFournisseur.gravure_marque,
        TypeFournisseur.metrologie,
        TypeFournisseur.controle_qualite,
        TypeFournisseur.logiciel_caao,
        TypeFournisseur.logiciel_support,
        TypeFournisseur.services_bureau_etude,
        TypeFournisseur.prestataire,
        TypeFournisseur.fabricant_machines,
        TypeFournisseur.maintenance_machine,
        TypeFournisseur.transport,
    ]
    return type_fournisseur in domaines


def suggestion_statut_automatique(commentaire: Optional[str] = None) -> StatutFournisseur:
    """
    Détermine un statut automatique du fournisseur selon son commentaire.
    """
    if commentaire:
        commentaire_lower = commentaire.lower()
        if "blacklist" in commentaire_lower or "fraude" in commentaire_lower:
            return StatutFournisseur.blacklisté
        if "inactif" in commentaire_lower or "fermé" in commentaire_lower:
            return StatutFournisseur.inactif
    return StatutFournisseur.actif


def enrichir_creation_fournisseur(data: FournisseurCreate) -> FournisseurCreate:
    """
    Applique des règles métier avant création : statut, pays par défaut, typage.
    """
    if not data.pays or data.pays.strip() == "":
        data.pays = "France"

    if not data.statut:
        data.statut = suggestion_statut_automatique(data.commentaire)

    return data