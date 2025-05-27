from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class AdresseClient(Base):
    __tablename__ = "adresses_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    type_adresse = Column(String(50), nullable=False, comment="facturation, livraison, siège, etc.")
    ligne_1 = Column(String(255), nullable=False)
    ligne_2 = Column(String(255), nullable=True)
    code_postal = Column(String(20), nullable=False)
    ville = Column(String(100), nullable=False)
    pays = Column(String(100), nullable=False, default="France")
    commentaire = Column(Text, nullable=True)
    principale = Column(Boolean, default=False)

    client = relationship("Client", back_populates="adresses")

    def __repr__(self):
        return f"<AdresseClient({self.type_adresse} - {self.ville})>"