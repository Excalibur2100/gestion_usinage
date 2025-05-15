from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Index, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class QrCodeObjet(Base):
    __tablename__ = "qr_codes_objets"

    id = Column(Integer, primary_key=True)

    objet_type = Column(String(50), nullable=False, comment="Type lié (ex: machine, outil, pièce)")
    objet_id = Column(Integer, nullable=False, comment="ID de l'objet")
    contenu = Column(Text, nullable=False, comment="Données contenues dans le QR code")
    
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Créé le")
    date_expiration = Column(DateTime, nullable=True, comment="Expire le (optionnel)")

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    utilisateur = relationship("Utilisateur", back_populates="qr_codes", lazy="joined")

    __mapper_args__ = {
        "polymorphic_on": objet_type,
        "polymorphic_identity": "qr_code_objet",
    }

    __table_args__ = (
        Index("idx_objet_type_id", "objet_type", "objet_id"),
        CheckConstraint(
            "objet_type IN ('machine', 'outil', 'piece', 'poste', 'facture')",
            name="check_qr_objet_type"
        ),
    )

    def __repr__(self):
        return f"<QRCodeObjet type={self.objet_type} id={self.objet_id}>"
