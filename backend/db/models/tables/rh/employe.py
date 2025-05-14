from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Employe(Base):
    __tablename__ = "employes"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'employé")
    prenom = Column(String(100), nullable=False, comment="Prénom de l'employé")
    email = Column(String(150), nullable=True, comment="Adresse email")
    telephone = Column(String(20), nullable=True, comment="Téléphone")
    date_naissance = Column(Date, nullable=False, comment="Date de naissance")
    numero_securite_sociale = Column(String(15), nullable=False, unique=True, comment="Numéro de sécurité sociale")
    adresse = Column(String(255), nullable=True, comment="Adresse")
    salaire = Column(Float, nullable=False, comment="Salaire brut mensuel")
    poste = Column(String(100), nullable=False, comment="Poste occupé")
    date_embauche = Column(Date, nullable=False, comment="Date d'embauche")
    date_fin_contrat = Column(Date, nullable=True, comment="Date de fin de contrat")
    
    # Relations
    productions = relationship("Production", back_populates="employe", cascade="all, delete-orphan")
    absences = relationship("Absence", back_populates="employe", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("salaire >= 0", name="check_salaire_employe"),
    )

    def __repr__(self):
        return (
            f"<Employe(id={self.id}, nom='{self.nom}', prenom='{self.prenom}', "
            f"poste='{self.poste}', salaire={self.salaire})>"
        )
