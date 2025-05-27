from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class HistoriqueClient(Base):
    __tablename__ = "historiques_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)

    type_action = Column(String(100), nullable=False, comment="appel, email, mise à jour, note, etc.")
    description = Column(Text, nullable=True)
    auteur = Column(String(100), nullable=True, comment="Nom de l'utilisateur ayant fait l'action")
    date_action = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    client = relationship("Client", back_populates="historiques")

    def __repr__(self):
        return f"<HistoriqueClient(client={self.client_id}, action='{self.type_action}')>"