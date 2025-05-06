from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= QR CODE OBJET =========================
class QrCodeObjet(Base):
    __tablename__ = "qr_codes_objets"

    id = Column(Integer, primary_key=True)
    objet_type = Column(
        String(50),
        nullable=False,
        comment="Type de l'objet associé (ex: machine, pièce, outil)",
    )
    objet_id = Column(Integer, nullable=False, comment="ID de l'objet associé")
    contenu = Column(Text, nullable=False, comment="Contenu encodé dans le QR code")
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création du QR code",
    )
    date_expiration = Column(
        DateTime, nullable=True, comment="Date d'expiration du QR code"
    )

    # Relations
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=True,
        comment="ID de l'utilisateur ayant généré le QR code",
    )
    utilisateur = relationship("Utilisateur", back_populates="qr_codes")

    # Polymorphisme
    __mapper_args__ = {
        "polymorphic_on": objet_type,
        "polymorphic_identity": "qr_code_objet",
    }
