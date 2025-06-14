from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    StatutAvoir,
    TypeAvoir
)
from datetime import datetime


def calculer_montant_ttc(montant_ht: float, taux_tva: float = 20.0) -> float:
    """
    Calcule le montant TTC à partir du montant HT et du taux de TVA.
    """
    return round(montant_ht * (1 + taux_tva / 100), 2)


def detecter_type_avoir(reference: str, motif: str) -> TypeAvoir:
    """
    Détecte automatiquement le type d’avoir en fonction du texte.
    """
    texte = (reference or "") + " " + (motif or "")
    texte = texte.lower()

    if "retour" in texte:
        return TypeAvoir.retour
    elif "remise" in texte:
        return TypeAvoir.remise
    elif "geste" in texte:
        return TypeAvoir.geste
    else:
        return TypeAvoir.autre


def statut_automatique_si_montant(montant: float) -> StatutAvoir:
    """
    Détermine automatiquement un statut en fonction du montant.
    """
    return StatutAvoir.brouillon if montant > 0 else StatutAvoir.annule


def suggere_avoir_auto(
    reference: str,
    fournisseur_id: int,
    montant_ht: float,
    taux_tva: float = 20.0,
    motif: str = "Avoir généré automatiquement"
) -> AvoirFournisseurCreate:
    """
    Génère automatiquement un objet AvoirFournisseurCreate intelligent.
    """
    montant_ttc = calculer_montant_ttc(montant_ht, taux_tva)
    statut = statut_automatique_si_montant(montant_ttc)
    type_avoir = detecter_type_avoir(reference, motif)

    return AvoirFournisseurCreate(
        reference=reference,
        reference_externe=None,
        fournisseur_id=fournisseur_id,
        utilisateur_id=None,
        commande_id=None,
        facture_id=None,
        document_lie_id=None,
        type_avoir=type_avoir,
        motif=motif,
        commentaire=None,
        categorie=None,
        tag=None,
        montant_ht=montant_ht,
        taux_tva=taux_tva,
        montant_ttc=montant_ttc,
        ecart_montant=None,
        devise="EUR",
        montant_devise_origine=None,
        taux_conversion=None,
        statut=statut,
        date_emission=datetime.utcnow(),
        date_remboursement=None,
        cree_par=None,
        modifie_par=None,
        version=1,
        etat_synchronisation="non_synchro",
        is_archived=False
    )