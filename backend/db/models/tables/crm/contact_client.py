from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ContactClient(Base):
    __tablename__ = "contacts_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)

    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=True)
    fonction = Column(String(100), nullable=True)
    email = Column(String(150), nullable=True)
    telephone = Column(String(50), nullable=True)
    principal = Column(Boolean, default=False)

    client = relationship("Client", back_populates="contacts")

    def __repr__(self):
        return f"<ContactClient({self.nom} {self.prenom})>"