from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class TagClient(Base):
    __tablename__ = "tags_clients"
    __table_args__ = (
        UniqueConstraint("client_id", "tag_id", name="uq_tag_client"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete="CASCADE"), nullable=False)

    client = relationship("Client", back_populates="tags")
    tag = relationship("Tag", back_populates="clients")

    def __repr__(self):
        return f"<TagClient(client_id={self.client_id}, tag_id={self.tag_id})>"