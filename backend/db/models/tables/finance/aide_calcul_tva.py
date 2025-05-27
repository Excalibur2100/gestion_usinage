from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from db.models.base import Base

class AideCalculTVA(Base):
    __tablename__ = "aide_calcul_tva"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    montant_ht = Column(Float, nullable=False, default=0.0)
    taux_tva = Column(Float, nullable=False, default=20.0, comment="Taux de TVA en %")
    montant_tva = Column(Float, nullable=False, default=0.0)
    montant_ttc = Column(Float, nullable=False, default=0.0)

    calcul_type = Column(String(50), default="HT→TTC", comment="HT→TTC ou TTC→HT")

    date_calcul = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<AideCalculTVA({self.calcul_type}, taux={self.taux_tva}%)>"