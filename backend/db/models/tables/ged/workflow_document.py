from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class WorkflowDocument(Base):
    __tablename__ = "workflows_documents"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents_qualite.id", ondelete="CASCADE"), nullable=False)
    workflow_id = Column(Integer, ForeignKey("workflows.id", ondelete="CASCADE"), nullable=False)

    statut = Column(String(50), nullable=False, default="en attente")
    date_liaison = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    document = relationship("DocumentQualite", back_populates="workflow_associe")
    workflow = relationship("Workflow", back_populates="documents_associes")

    def __repr__(self):
        return f"<WorkflowDocument(document_id={self.document_id}, workflow_id={self.workflow_id}, statut='{self.statut}')>"