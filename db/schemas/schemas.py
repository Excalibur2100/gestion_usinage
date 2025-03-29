from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

# ========================= UTILISATEUR =========================

class UtilisateurBase(BaseModel):
    nom: str
    email: EmailStr
    role: str

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str = Field(..., min_length=8)

class UtilisateurUpdate(BaseModel):
    nom: Optional[str] = None
    email: Optional[EmailStr] = None
    mot_de_passe: Optional[str] = Field(None, min_length=8)
    role: Optional[str] = None
    actif: Optional[bool] = None

class UtilisateurRead(BaseModel):
    id: int
    nom: str
    email: str
    role: str
    actif: bool

    class Config:
        orm_mode = True 
        

# ========================= DROIT =========================
class DroitBase(BaseModel):
    module: str
    autorisation: bool = False

class DroitCreate(DroitBase):
    utilisateur_id: int

class DroitRead(DroitBase):
    id: int
    utilisateur_id: int

    class Config:
        orm_mode = True
        

# ========================= CLIENT =========================
class ClientBase(BaseModel):
    nom: str
    email: Optional[str]
    telephone: Optional[str]
    adresse: Optional[str]
    siret: Optional[str]
    tva_intracom: Optional[str]
    secteur_activite: Optional[str]
    site_web: Optional[str]
    commentaire: Optional[str]

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= FOURNISSEUR =========================
class FournisseurBase(BaseModel):
    nom: str
    contact: Optional[str]
    email: Optional[str]
    telephone: Optional[str]
    adresse: Optional[str]
    tva: Optional[str]
    site_web: Optional[str]
    catalogue_interactif: Optional[str]

class FournisseurCreate(FournisseurBase):
    pass

class FournisseurRead(FournisseurBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= DEVIS =========================
class DevisBase(BaseModel):
    client_id: int
    date_devis: datetime
    montant_total: float
    statut: str
    scenarios: Optional[str]

class DevisCreate(DevisBase):
    pass

class DevisRead(DevisBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= COMMANDE =========================
class CommandeBase(BaseModel):
    client_id: int
    statut: str = "en attente"
    date_commande: datetime
    bon_commande_client: Optional[str]

class CommandeCreate(CommandeBase):
    pass

class CommandeRead(CommandeBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= FACTURE =========================
class FactureBase(BaseModel):
    numero_facture: str
    client_id: int
    commande_id: Optional[int]
    date_emission: datetime
    date_echeance: Optional[datetime]
    montant_total: float
    statut: str = "En attente"
    observations: Optional[str]

class FactureCreate(FactureBase):
    pass

class FactureRead(FactureBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= MACHINE =========================
class MachineBase(BaseModel):
    nom: str
    type: str
    vitesse_max: Optional[float]
    puissance: Optional[float]

class MachineCreate(MachineBase):
    pass

# ========================= PLANNING MACHINE =========================
class PlanningMachineBase(BaseModel):
    machine_id: int
    date: datetime
    plage_horaire: str
    tache: Optional[str]

class PlanningMachineCreate(PlanningMachineBase):
    pass

class PlanningMachineRead(PlanningMachineBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= PLANNING EMPLOYÉ =========================
class PlanningEmployeBase(BaseModel):
    utilisateur_id: int
    machine_id: Optional[int]
    date: datetime
    plage_horaire: Optional[str]
    tache: Optional[str]
    statut: str = "Prévu"

class PlanningEmployeCreate(PlanningEmployeBase):
    pass

class PlanningEmployeRead(PlanningEmployeBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= GAMME PRODUCTION =========================
class GammeProductionBase(BaseModel):
    piece_id: int
    ordre: int
    machine_id: Optional[int]
    outil_id: Optional[int]
    materiau_id: Optional[int]
    operation: str
    temps_prevu: Optional[float]
    temps_reel: Optional[float]
    statut: str = "En attente"

class GammeProductionCreate(GammeProductionBase):
    pass

class GammeProductionRead(GammeProductionBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= PIECE =========================
class PieceBase(BaseModel):
    nom: str
    numero_plan: str
    description: Optional[str]

class PieceCreate(PieceBase):
    pass

class PieceRead(PieceBase):
    id: int

    class Config:
        orm_mode = True
        

# ========================= PROGRAMME PIECE =========================
class ProgrammePieceBase(BaseModel):
    piece_id: int
    nom_programme: str
    fichier_path: str
    postprocesseur_id: Optional[int]
    date_import: datetime

class ProgrammePieceCreate(ProgrammePieceBase):
    pass

class ProgrammePieceRead(ProgrammePieceBase):
    id: int

    class Config:
        orm_mode = True
        

class CommandePieceCreate(BaseModel):
    nom: str
    description: str

class CommandePieceRead(BaseModel):
    id: int
    nom: str
    description: str

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class GestionAccesCreate(BaseModel):
    utilisateur_id: int
    role: str

class GestionAccesRead(BaseModel):
    id: int
    utilisateur_id: int
    role: str

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class PlanningMachineCreate(BaseModel):
    debut: datetime
    fin: datetime
    machine_id: int

class PlanningMachineRead(BaseModel):
    id: int
    debut: datetime
    fin: datetime
    machine_id: int

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class GestionFiltrageCreate(BaseModel):
    filtre: str
    valeur: str

class GestionFiltrageRead(BaseModel):
    id: int
    filtre: str
    valeur: str

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2
        
class ChargeMachineCreate(BaseModel):
    machine_id: int
    charge: float
    date: datetime

class ChargeMachineRead(BaseModel):
    id: int
    machine_id: int
    charge: float
    date: datetime

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class SurveillanceCameraCreate(BaseModel):
    camera_id: int
    emplacement: str
    statut: str

class SurveillanceCameraRead(BaseModel):
    id: int
    camera_id: int
    emplacement: str
    statut: str

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class ControleRobotCreate(BaseModel):
    robot_id: int
    action: str
    statut: str

class ControleRobotRead(BaseModel):
    id: int
    robot_id: int
    action: str
    statut: str

    class Config:
        orm_mode = True  # Remplace `orm_mode` dans Pydantic v2

class MachineRead(BaseModel):
    id: int
    nom: str

    class Config:
        orm_mode = True

