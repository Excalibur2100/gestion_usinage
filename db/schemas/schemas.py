from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# ========================= DROITS D'ACCÈS =========================
class DroitAccesBase(BaseModel):
    module: str
    peut_lire: bool = False
    peut_creer: bool = False
    peut_modifier: bool = False
    peut_supprimer: bool = False
    acces_total: bool = False

class DroitAccesCreate(DroitAccesBase):
    utilisateur_id: int

class DroitAccesRead(DroitAccesBase):
    id: int
    utilisateur_id: int

    class Config:
        orm_mode = True

# ========================= UTILISATEUR =========================
class UtilisateurBase(BaseModel):
    nom: str
    email: EmailStr
    role: str
    actif: bool = True

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str

class UtilisateurRead(UtilisateurBase):
    id: int
    droits: Optional[List[DroitAccesRead]] = []

    class Config:
        orm_mode = True

# ========================= RH =========================
class RHBase(BaseModel):
    poste: Optional[str]
    contrat: Optional[str]
    temps_travail: Optional[float]
    est_cadre: Optional[bool]
    date_debut: Optional[datetime]
    salaire_brut: Optional[float]
    statut_administratif: Optional[str]
    remarques: Optional[str]

class RHCreate(RHBase):
    utilisateur_id: int

class RHRead(RHBase):
    id: int
    utilisateur_id: int

    class Config:
        orm_mode = True
# ========================= CLIENT =========================
class ClientBase(BaseModel):
    nom: str
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    adresse: Optional[str] = None
    siret: Optional[str] = None
    tva_intracom: Optional[str] = None
    secteur_activite: Optional[str] = None
    site_web: Optional[str] = None
    commentaire: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int

    class Config:
        orm_mode = True

# ========================= FOURNISSEUR =========================
class FournisseurBase(BaseModel):
    nom: str
    contact: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    adresse: Optional[str] = None
    tva: Optional[str] = None
    site_web: Optional[str] = None
    catalogue_interactif: Optional[str] = None

class FournisseurCreate(FournisseurBase):
    pass

class FournisseurRead(FournisseurBase):
    id: int

    class Config:
        orm_mode = True

# ========================= ÉVALUATION FOURNISSEUR =========================
class EvaluationFournisseurBase(BaseModel):
    date_evaluation: Optional[datetime] = None
    critere: Optional[str]
    note: Optional[float]
    commentaire: Optional[str] = None

class EvaluationFournisseurCreate(EvaluationFournisseurBase):
    fournisseur_id: int

class EvaluationFournisseurRead(EvaluationFournisseurBase):
    id: int
    fournisseur_id: int

    class Config:
        orm_mode = True

# ========================= DEVIS =========================
class DevisBase(BaseModel):
    date_devis: Optional[datetime] = None
    montant_total: Optional[float] = None
    statut: Optional[str] = None
    scenarios: Optional[str] = None

class DevisCreate(DevisBase):
    client_id: int

class DevisRead(DevisBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True

# ========================= COMMANDE =========================
class CommandeBase(BaseModel):
    statut: Optional[str] = "en attente"
    date_commande: Optional[datetime] = None
    bon_commande_client: Optional[str] = None
    forcer_creation: Optional[bool] = False

class CommandeCreate(CommandeBase):
    client_id: int

class CommandeRead(CommandeBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True

# ========================= LIGNE DE COMMANDE (CommandePiece) =========================
class CommandePieceBase(BaseModel):
    quantite: int

class CommandePieceCreate(CommandePieceBase):
    commande_id: int
    piece_id: int

class CommandePieceRead(CommandePieceBase):
    id: int
    commande_id: int
    piece_id: int

    class Config:
        orm_mode = True

# ========================= PIECE =========================
class PieceBase(BaseModel):
    nom: Optional[str]
    numero_plan: Optional[str]
    description: Optional[str]

class PieceCreate(PieceBase):
    pass

class PieceRead(PieceBase):
    id: int

    class Config:
        orm_mode = True

# ========================= GAMME PRODUCTION =========================
class GammeProductionBase(BaseModel):
    ordre: Optional[int]
    operation: Optional[str]
    temps_prevu: Optional[float]
    temps_reel: Optional[float]
    statut: Optional[str] = "En attente"
    moyen_controle: Optional[str]
    programme_piece: Optional[str]
    longueur_debit: Optional[float]
    nombre_debits: Optional[int]

class GammeProductionCreate(GammeProductionBase):
    piece_id: int
    machine_id: int
    outil_id: int
    materiau_id: int

class GammeProductionRead(GammeProductionBase):
    id: int
    piece_id: int
    machine_id: int
    outil_id: int
    materiau_id: int

    class Config:
        orm_mode = True

# ========================= MATERIAU =========================
class MateriauBase(BaseModel):
    nom: str
    afnor: Optional[str]
    stock: Optional[int]
    durete: Optional[str]
    type: Optional[str] = "Acier"
    est_aeronautique: Optional[bool] = False
    certificat_matiere: Optional[str]

class MateriauCreate(MateriauBase):
    fournisseur_id: int

class MateriauRead(MateriauBase):
    id: int
    fournisseur_id: int

    class Config:
        orm_mode = True

# ========================= COMMANDE PIECE =========================
class CommandePieceBase(BaseModel):
    quantite: int

class CommandePieceCreate(CommandePieceBase):
    commande_id: int
    piece_id: int

class CommandePieceRead(CommandePieceBase):
    id: int
    commande_id: int
    piece_id: int

    class Config:
        orm_mode = True


# ========================= MACHINE =========================
class MachineBase(BaseModel):
    nom: Optional[str]
    type: Optional[str]
    vitesse_max: Optional[float]
    puissance: Optional[float]
    nb_axes: Optional[int]
    axe_x_max: Optional[float]
    axe_y_max: Optional[float]
    axe_z_max: Optional[float]
    commande_numerique: Optional[str]
    post_processeur: Optional[str]
    logiciel_fao: Optional[str]

class MachineCreate(MachineBase):
    pass

class MachineRead(MachineBase):
    id: int

    class Config:
        orm_mode = True

# ========================= OUTIL =========================
class OutilBase(BaseModel):
    nom: Optional[str]
    type: Optional[str]
    stock: Optional[int]
    en_stock: Optional[bool]
    diametre: Optional[float]
    longueur: Optional[float]
    ref_fournisseur: Optional[str]
    catalogue_url: Optional[str]

class OutilCreate(OutilBase):
    fournisseur_id: int

class OutilRead(OutilBase):
    id: int
    fournisseur_id: int

    class Config:
        orm_mode = True

# ========================= INSTRUMENT DE CONTROLE =========================
class InstrumentControleBase(BaseModel):
    nom: Optional[str]
    type_instrument: Optional[str]
    numero_serie: Optional[str]
    date_calibrage: Optional[datetime]
    date_prochaine_calibration: Optional[datetime]
    conforme_qhse: Optional[bool] = True
    en_service: Optional[bool] = True

class InstrumentControleCreate(InstrumentControleBase):
    pass

class InstrumentControleRead(InstrumentControleBase):
    id: int

    class Config:
        orm_mode = True

# ========================= CONTROLE PIECE =========================
class ControlePieceBase(BaseModel):
    resultat: Optional[str]
    date_controle: Optional[datetime]
    remarque: Optional[str]

class ControlePieceCreate(ControlePieceBase):
    instrument_id: int
    piece_id: int

class ControlePieceRead(ControlePieceBase):
    id: int
    instrument_id: int
    piece_id: int

    class Config:
        orm_mode = True

# ========================= FACTURE =========================
class FactureBase(BaseModel):
    numero_facture: str
    date_emission: Optional[datetime]
    date_echeance: Optional[datetime]
    montant_total: Optional[float]
    statut: Optional[str] = "En attente"
    mode_generation: Optional[str] = "Automatique"
    observations: Optional[str]

class FactureCreate(FactureBase):
    client_id: int
    commande_id: int

class FactureRead(FactureBase):
    id: int
    client_id: int
    commande_id: int
    valide_par: Optional[int]

    class Config:
        orm_mode = True

# ========================= PROGRAMME PIECE =========================
class ProgrammePieceBase(BaseModel):
    nom_programme: str
    fichier_path: str
    date_import: Optional[datetime]

class ProgrammePieceCreate(ProgrammePieceBase):
    piece_id: int
    postprocesseur_id: int

class ProgrammePieceRead(ProgrammePieceBase):
    id: int
    piece_id: int
    postprocesseur_id: int

    class Config:
        orm_mode = True

# ========================= POST-PROCESSEUR =========================
class PostProcesseurBase(BaseModel):
    nom: str
    logiciel_fao: str
    extension_sortie: Optional[str]
    configuration: Optional[str]
    date_creation: Optional[datetime]

class PostProcesseurCreate(PostProcesseurBase):
    machine_id: int

class PostProcesseurRead(PostProcesseurBase):
    id: int
    machine_id: int

    class Config:
        orm_mode = True

# ========================= PLANNING MACHINE =========================
class PlanningMachineBase(BaseModel):
    date: datetime
    plage_horaire: str
    tache: Optional[str]
    statut: Optional[str]
    charge_estimee: Optional[float]

class PlanningMachineCreate(PlanningMachineBase):
    machine_id: int
    gamme_id: int

class PlanningMachineRead(PlanningMachineBase):
    id: int
    machine_id: int
    gamme_id: int

    class Config:
        orm_mode = True

# ========================= PLANNING EMPLOYÉ =========================
class PlanningEmployeBase(BaseModel):
    date: datetime
    plage_horaire: str
    tache: Optional[str]
    statut: Optional[str]
    affectation_auto: Optional[bool] = True

class PlanningEmployeCreate(PlanningEmployeBase):
    utilisateur_id: int
    machine_id: Optional[int]

class PlanningEmployeRead(PlanningEmployeBase):
    id: int
    utilisateur_id: int
    machine_id: Optional[int]

    class Config:
        orm_mode = True

# ========================= POINTAGE =========================
class PointageBase(BaseModel):
    date_pointage: Optional[datetime]
    heure_debut: datetime
    heure_fin: Optional[datetime]
    duree_effective: Optional[float]
    remarques: Optional[str]

class PointageCreate(PointageBase):
    utilisateur_id: int
    machine_id: int
    gamme_id: int

class PointageRead(PointageBase):
    id: int
    utilisateur_id: int
    machine_id: int
    gamme_id: int

    class Config:
        orm_mode = True

# ========================= MAINTENANCE =========================
class MaintenanceBase(BaseModel):
    type_maintenance: str
    date_planifiee: datetime
    date_reelle: Optional[datetime]
    statut: Optional[str]
    description: Optional[str]
    remarques: Optional[str]

class MaintenanceCreate(MaintenanceBase):
    machine_id: int
    operateur_id: Optional[int]

class MaintenanceRead(MaintenanceBase):
    id: int
    machine_id: int
    operateur_id: Optional[int]

    class Config:
        orm_mode = True

# ========================= CHARGE MACHINE =========================
class ChargeMachineBase(BaseModel):
    date: datetime
    charge_totale: float
    seuil_surcharge: Optional[float] = 7.5

class ChargeMachineCreate(ChargeMachineBase):
    machine_id: int

class ChargeMachineRead(ChargeMachineBase):
    id: int
    machine_id: int

    class Config:
        orm_mode = True

# ========================= AUDIT QUALITÉ =========================
class AuditQualiteBase(BaseModel):
    date: datetime
    type_audit: str
    responsable: str
    remarques: Optional[str]
    statut: Optional[str]

class AuditQualiteCreate(AuditQualiteBase):
    document_id: int

class AuditQualiteRead(AuditQualiteBase):
    id: int
    document_id: int

    class Config:
        orm_mode = True

# ========================= NON CONFORMITÉ =========================
class NonConformiteBase(BaseModel):
    origine: str
    description: Optional[str]
    action_corrective: Optional[str]
    date_detection: datetime
    date_resolution: Optional[datetime]
    statut: Optional[str] = "Ouvert"

class NonConformiteCreate(NonConformiteBase):
    utilisateur_id: int
    machine_id: Optional[int]
    materiau_id: Optional[int]
    outil_id: Optional[int]
    instrument_id: Optional[int]

class NonConformiteRead(NonConformiteBase):
    id: int
    utilisateur_id: int
    machine_id: Optional[int]
    materiau_id: Optional[int]
    outil_id: Optional[int]
    instrument_id: Optional[int]

    class Config:
        orm_mode = True

# ========================= DOCUMENT QUALITÉ =========================
class DocumentQualiteBase(BaseModel):
    titre: str
    type_document: str
    reference_norme: Optional[str]
    fichier_path: str
    version: Optional[str]
    date_ajout: Optional[datetime]
    actif: Optional[bool] = True

class DocumentQualiteCreate(DocumentQualiteBase):
    pass

class DocumentQualiteRead(DocumentQualiteBase):
    id: int

    class Config:
        orm_mode = True

# ========================= DOCUMENT RÉGLEMENTAIRE =========================
class DocumentReglementaireBase(BaseModel):
    titre: str
    description: Optional[str]
    type_document: str
    date_edition: datetime
    valide_jusquau: Optional[datetime]
    fichier_stocke: str
    conforme: Optional[bool] = True
    norme_associee: Optional[str]

class DocumentReglementaireCreate(DocumentReglementaireBase):
    utilisateur_id: Optional[int]

class DocumentReglementaireRead(DocumentReglementaireBase):
    id: int
    utilisateur_id: Optional[int]

    class Config:
        orm_mode = True

# ========================= HISTORIQUE D'ACTION =========================
class HistoriqueActionBase(BaseModel):
    module: str
    action: str
    details: Optional[str]
    date_action: Optional[datetime]

class HistoriqueActionCreate(HistoriqueActionBase):
    utilisateur_id: int

class HistoriqueActionRead(HistoriqueActionBase):
    id: int
    utilisateur_id: int

    class Config:
        orm_mode = True

# ========================= GESTION ACCÈS =========================
class GestionAccesBase(BaseModel):
    module: str
    peut_lire: bool = False
    peut_ecrire: bool = False
    peut_supprimer: bool = False
    peut_valider: bool = False

class GestionAccesCreate(GestionAccesBase):
    utilisateur_id: int

class GestionAccesRead(GestionAccesBase):
    id: int
    utilisateur_id: int

    class Config:
        orm_mode = True

# ========================= QR CODE OBJET =========================
class QrCodeObjetBase(BaseModel):
    objet_type: str
    objet_id: int
    qr_code_data: str
    date_creation: Optional[datetime]

class QrCodeObjetCreate(QrCodeObjetBase):
    pass

class QrCodeObjetRead(QrCodeObjetBase):
    id: int

    class Config:
        orm_mode = True

# ========================= FINANCE =========================
class FinanceBase(BaseModel):
    type_transaction: str
    categorie: Optional[str]
    sous_categorie: Optional[str]
    description: Optional[str]
    montant: float
    devise: Optional[str] = "EUR"
    date: Optional[datetime]
    periode: Optional[str]  # Format "YYYY-MM"
    statut: Optional[str] = "Validé"
    moyen_paiement: Optional[str]
    justificatif: Optional[str]
    reference_facture: Optional[str]

class FinanceCreate(FinanceBase):
    utilisateur_id: int
    fournisseur_id: Optional[int]
    materiau_id: Optional[int]
    piece_id: Optional[int]
    instrument_id: Optional[int]
    outil_id: Optional[int]
    machine_id: Optional[int]
    facture_id: Optional[int]

class FinanceRead(FinanceBase):
    id: int
    utilisateur_id: int
    fournisseur_id: Optional[int]
    materiau_id: Optional[int]
    piece_id: Optional[int]
    instrument_id: Optional[int]
    outil_id: Optional[int]
    machine_id: Optional[int]
    facture_id: Optional[int]

    class Config:
        orm_mode = True

# ========================= STATISTIQUES FINANCIÈRES =========================

class StatFinanceBase(BaseModel):
    periode: str
    type_stat: str
    categorie: Optional[str]
    sous_categorie: Optional[str]
    montant_total: float
    devise: Optional[str] = "EUR"
    precision: Optional[str] = "mois"
    date_calcul: Optional[datetime]

class StatFinanceCreate(StatFinanceBase):
    source_finance_id: Optional[int] = None

class StatFinanceRead(StatFinanceBase):
    id: int
    source_finance_id: Optional[int]

    class Config:
        orm_mode = True



