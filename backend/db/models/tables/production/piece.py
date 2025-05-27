from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Piece(Base):
    __tablename__ = "pieces"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom de la pièce")
    description = Column(Text, nullable=True, comment="Détail ou notes sur la pièce")
    reference = Column(String(100), nullable=True, unique=True, comment="Référence interne ou client")
    matiere = Column(String(100), nullable=True, comment="Matière utilisée")
    quantite = Column(Integer, default=1, comment="Quantité prévue ou standard")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'enregistrement")

    client_id = Column(
        Integer, ForeignKey("clients.id", ondelete="SET NULL"),
        nullable=True, index=True, comment="Client concerné"
    )

    # ------------------------------------------------------------
    # RELATIONS INTERNES PRODUCTION
    # ------------------------------------------------------------
    client = relationship("Client", back_populates="pieces", lazy="joined")

    programmes = relationship("ProgrammePiece", back_populates="piece", cascade="all, delete-orphan")
    gammes = relationship("GammeProduction", back_populates="piece", cascade="all, delete-orphan")
    outils = relationship("LiaisonPieceOutil", back_populates="piece", cascade="all, delete-orphan")
    ordres_fabrication = relationship("OrdreFabrication", back_populates="piece", cascade="all, delete-orphan")

    # ------------------------------------------------------------
    # RELATIONS TRANSVERSALES (QA / IA / GED / TRACABILITE / QUALITE)
    # ------------------------------------------------------------
    commandes = relationship("CommandePiece", back_populates="piece", cascade="all, delete-orphan")
    productions = relationship("Production", back_populates="piece", cascade="all, delete-orphan")
    tracabilites = relationship("Tracabilite", back_populates="piece", cascade="all, delete-orphan")

    non_conformites = relationship("NonConformite", back_populates="piece", cascade="all, delete-orphan")
    fiches_controle = relationship("FicheSuiviControle", back_populates="piece", cascade="all, delete-orphan")
    analyses = relationship("AnalyseFichier", back_populates="piece", cascade="all, delete-orphan")

    piece_ouvertes = relationship("PieceOuverte", back_populates="piece", cascade="all, delete-orphan")
    piece_faites = relationship("PieceFait", back_populates="piece", cascade="all, delete-orphan")
    piece_fermetures = relationship("PieceFermeture", back_populates="piece", cascade="all, delete-orphan")

    historiques_chiffrage = relationship("HistoriqueChiffrage", back_populates="piece", cascade="all, delete-orphan")
    suggestions_ia = relationship("SuggestionOutil", back_populates="piece", cascade="all, delete-orphan")

    documents = relationship("WorkflowDocument", back_populates="piece", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Piece id={self.id} nom='{self.nom}' client_id={self.client_id}>"

    def get_programmes(self):
        return [p.nom for p in self.programmes]