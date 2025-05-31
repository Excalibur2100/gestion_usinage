from typing import List, Optional
from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    TypeAvoir
)

def calculer_montant_ttc(montant_ht: float, taux_tva: float) -> float:
    """
    Calcule le montant TTC à partir du HT et du taux de TVA.
    """
    return round(montant_ht * (1 + taux_tva / 100), 2)


def detecter_type_avoir(reference: str = "", motif: Optional[str] = "") -> TypeAvoir:
    """
    Déduit automatiquement le type d'avoir en analysant la référence ou le motif.
    """
    ref = reference.lower() if reference else ""
    motif = motif.lower() if motif else ""

    if "retour" in motif or "marchandise" in motif or "retourné" in ref:
        return TypeAvoir.retour
    elif "remise" in motif or "rabais" in motif:
        return TypeAvoir.remise
    elif "geste" in motif or "commercial" in motif:
        return TypeAvoir.geste
    return TypeAvoir.autre


def suggere_avoir_auto(
    facture_id: int,
    total_rembourse: float,
    raison: Optional[str] = None,
    fournisseur_id: int = 1
) -> AvoirFournisseurCreate:
    """
    Génère automatiquement une suggestion d'avoir fournisseur.
    """
    montant_ht = round(total_rembourse / 1.2, 2)
    tva = 20.0
    return AvoirFournisseurCreate(
        reference=f"SUGG-AVF-{facture_id}",
        fournisseur_id=fournisseur_id,
        utilisateur_id=None,
        facture_id=facture_id,
        reference_externe=None,
        montant_ht=montant_ht,
        taux_tva=tva,
        montant_ttc=calculer_montant_ttc(montant_ht, tva),
        type_avoir=detecter_type_avoir("", raison),
        commentaire="Suggestion IA automatique",
        motif=raison,
        cree_par=0
    )