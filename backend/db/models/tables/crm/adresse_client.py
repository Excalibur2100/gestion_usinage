from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class AdresseClient(Base):
    __tablename__ = "adresse_client"
    __table_args__ = (
        {"comment": "Table des adresses associées aux clients, pour facturation et livraison."},
    )

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    type_adresse = Column(String(50), nullable=False, comment="facturation / livraison")
    adresse = Column(String(255), nullable=False)
    code_postal = Column(String(10), nullable=True)
    ville = Column(String(100), nullable=True)
    pays = Column(String(100), default="France")

    client = relationship("Client", back_populates="adresses", lazy="selectin")

    def __repr__(self):
        return f"<AdresseClient(id={self.id}, client_id={self.client_id}, type='{self.type_adresse}')>"

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "type_adresse": self.type_adresse,
            "adresse": self.adresse,
            "code_postal": self.code_postal,
            "ville": self.ville,
            "pays": self.pays,
        }
