from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class UtilisateurSite(Base):
    __tablename__ = "utilisateurs_sites"
    __table_args__ = (
        UniqueConstraint("utilisateur_id", "site_id", name="uq_utilisateur_site"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)
    site_id = Column(Integer, ForeignKey("sites.id", ondelete="CASCADE"), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="sites")
    site = relationship("Site", back_populates="utilisateurs")

    def __repr__(self):
        return f"<UtilisateurSite(utilisateur={self.utilisateur_id}, site={self.site_id})>"