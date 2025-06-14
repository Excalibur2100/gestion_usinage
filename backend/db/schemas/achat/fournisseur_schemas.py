from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

# -------- ENUM --------
class TypeFournisseur(str, Enum):
    fabricant_machines = "fabricant_machines"
    fournisseur_matiere_premiere = "fournisseur_matiere_premiere"
    fournisseur_acier = "fournisseur_acier"
    fournisseur_inox = "fournisseur_inox"
    fournisseur_non_ferreux = "fournisseur_non_ferreux"
    fournisseur_outillage = "fournisseur_outillage"
    fournisseur_outils_de_mesure = "fournisseur_outils_de_mesure"
    fournisseur_equipements_de_protection = "fournisseur_equipements_de_protection"
    fournisseur_composants_standard = "fournisseur_composants_standard"
    fournisseur_generaliste = "fournisseur_generaliste"
    outilleur = "outilleur"
    machine_outil = "machine_outil"
    transport = "transport"
    controle_qualite = "controle_qualite"
    metrologie = "metrologie"
    logiciel_support = "logiciel_support"
    logiciel_caao = "logiciel_caao"
    services_bureau_etude = "services_bureau_etude"
    sous_traitant_usinage = "sous_traitant_usinage"
    sous_traitant_fraisage = "sous_traitant_fraisage"
    sous_traitant_tournage = "sous_traitant_tournage"
    sous_traitant_edm = "sous_traitant_edm"
    sous_traitant_soudure = "sous_traitant_soudure"
    traitement_thermique = "traitement_thermique"
    traitement_surface = "traitement_surface"
    peinture_industrielle = "peinture_industrielle"
    gravure_marque = "gravure_marque"
    maintenance_machine = "maintenance_machine"
    prestataire_logistique = "prestataire_logistique"
    prestataire = "prestataire"
    grossiste = "grossiste"
    distributeur = "distributeur"
    integrateur = "integrateur"
    autre = "autre"

class StatutFournisseur(str, Enum):
    actif = "actif"
    inactif = "inactif"
    blacklisté = "blacklisté"

# -------- BASE --------
class FournisseurBase(BaseModel):
    nom: str = Field(..., description="Nom du fournisseur, ex: Fournisseur Métaux Usinés")
    code: Optional[str] = Field(None, description="Code du fournisseur, ex: FRN-001")

    type: TypeFournisseur = Field(default=TypeFournisseur.autre)
    statut: StatutFournisseur = Field(default=StatutFournisseur.actif)

    adresse: Optional[str] = Field(None, description="Adresse du fournisseur, ex: 123 rue de l'industrie")
    ville: Optional[str] = Field(None, description="Ville du fournisseur, ex: Metz")
    code_postal: Optional[str] = Field(None, description="Code postal du fournisseur, ex: 57000")
    pays: Optional[str] = Field(default="France", description="Pays du fournisseur, ex: France")

    email: Optional[EmailStr] = Field(None, description="Adresse email du fournisseur, ex: contact@fournisseur.fr")
    telephone: Optional[str] = Field(None, description="Téléphone du fournisseur, ex: +33 3 87 00 00 00")
    site_web: Optional[str] = Field(None, description="Site web du fournisseur, ex: https://www.fournisseur.fr")

    contact_nom: Optional[str] = Field(None, description="Nom du contact, ex: Jean DUPONT")
    contact_email: Optional[EmailStr] = Field(None, description="Email du contact, ex: jean.dupont@fournisseur.fr")
    contact_telephone: Optional[str] = Field(None, description="Téléphone du contact, ex: +33 6 12 34 56 78")

    commentaire: Optional[str] = None
    actif: Optional[bool] = True

    cree_par: Optional[int] = None
    modifie_par: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True

# -------- CREATE --------
class FournisseurCreate(FournisseurBase):
    pass

# -------- UPDATE --------
class FournisseurUpdate(BaseModel):
    nom: Optional[str] = None
    code: Optional[str] = None
    type: Optional[TypeFournisseur] = None
    statut: Optional[StatutFournisseur] = None
    adresse: Optional[str] = None
    ville: Optional[str] = None
    code_postal: Optional[str] = None
    pays: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    site_web: Optional[str] = None
    contact_nom: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    contact_telephone: Optional[str] = None
    commentaire: Optional[str] = None
    actif: Optional[bool] = None
    modifie_par: Optional[int] = None

# -------- READ --------
class FournisseurRead(FournisseurBase):
    id: int
    uuid: Optional[str] = None
    timestamp_creation: Optional[datetime] = None
    timestamp_modification: Optional[datetime] = None

# -------- DETAIL --------
class FournisseurDetail(FournisseurRead):
    auteur_creation_nom: Optional[str] = None
    auteur_modification_nom: Optional[str] = None

# -------- LIST --------
class FournisseurList(BaseModel):
    id: int
    nom: str
    code: Optional[str]
    type: TypeFournisseur
    statut: StatutFournisseur

    class Config:
        orm_mode = True
        from_attributes = True

# -------- SEARCH --------
class FournisseurSearch(BaseModel):
    nom: Optional[str] = None
    code: Optional[str] = None
    type: Optional[TypeFournisseur] = None
    statut: Optional[StatutFournisseur] = None
    pays: Optional[str] = None
    actif: Optional[bool] = None

# -------- RESPONSE --------
class FournisseurResponse(BaseModel):
    message: str
    fournisseur: Optional[FournisseurRead]

# -------- BULK --------
class FournisseurBulkCreate(BaseModel):
    fournisseurs: List[FournisseurCreate]

class FournisseurBulkDelete(BaseModel):
    ids: List[int]

# -------- SEARCH RESULTS --------
class FournisseurSearchResults(BaseModel):
    total: int
    results: List[FournisseurRead]