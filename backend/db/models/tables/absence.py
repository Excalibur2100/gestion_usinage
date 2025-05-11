from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Absence(Base):
    __tablename__ = "absences"

    id = Column(Integer, primary_key=True, index=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False, comment="ID de l'employé concerné")
    
    date_debut = Column(Date, nullable=False, comment="Début de l'absence")
    date_fin = Column(Date, nullable=False, comment="Fin de l'absence")
    type_absence = Column(String(50), nullable=False, comment="Type : congé, maladie, RTT, etc.")
    statut = Column(String(30), default="en attente", comment="Statut : en attente, validée, refusée")
    justificatif_url = Column(String(255), nullable=True, comment="Fichier PDF ou lien justificatif")
    is_paid = Column(String(5), default="oui", comment="Absence rémunérée : oui/non")
    commentaire = Column(Text, nullable=True, comment="Commentaire RH ou manager")
    employe_id = Column(Integer, ForeignKey("employes.id", ondelete="CASCADE"))
    employe = relationship("Employe", back_populates="absences", lazy="joined")


    utilisateur = relationship("Utilisateur", back_populates="absences", lazy="joined")

    def __repr__(self):
        return f"<Absence employe={self.employe.id} {self.date_debut} - {self.date_fin}>"