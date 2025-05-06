from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Employe(Base):
    """
    Classe Employe représentant un employé dans le système.

    Attributs :
        - id : Identifiant unique de l'employé.
        - nom : Nom de l'employé.
        - prenom : Prénom de l'employé.
        - email : Adresse email de l'employé.
        - telephone : Numéro de téléphone de l'employé.
        - date_naissance : Date de naissance de l'employé.
        - numero_securite_sociale : Numéro de sécurité sociale de l'employé.
        - adresse : Adresse de l'employé.
        - salaire : Salaire brut mensuel de l'employé.
        - poste : Poste occupé par l'employé.
        - date_embauche : Date d'embauche de l'employé.
        - date_fin_contrat : Date de fin de contrat (si applicable).
    """
    __tablename__ = "employes"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'employé")
    prenom = Column(String(100), nullable=False, comment="Prénom de l'employé")
    email = Column(String(150), nullable=True, comment="Adresse email de l'employé")
    telephone = Column(String(20), nullable=True, comment="Numéro de téléphone de l'employé")
    date_naissance = Column(Date, nullable=False, comment="Date de naissance de l'employé")
    numero_securite_sociale = Column(
        String(15), nullable=False, unique=True, comment="Numéro de sécurité sociale de l'employé"
    )
    adresse = Column(String(255), nullable=True, comment="Adresse de l'employé")
    salaire = Column(Float, nullable=False, comment="Salaire brut mensuel de l'employé")
    poste = Column(String(100), nullable=False, comment="Poste occupé par l'employé")
    date_embauche = Column(Date, nullable=False, comment="Date d'embauche de l'employé")
    date_fin_contrat = Column(Date, nullable=True, comment="Date de fin de contrat (si applicable)")

    # Relations
    productions = relationship("Production", back_populates="employe")
    absences = relationship("Absence", back_populates="employe")

    def __repr__(self):
        return (
            f"<Employe(id={self.id}, nom='{self.nom}', prenom='{self.prenom}', "
            f"poste='{self.poste}', salaire={self.salaire})>"
        )