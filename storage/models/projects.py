import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from storage.database import manager
from utils import datetime


class Project(manager.Base):
    __tablename__ = "project"
    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True,
                default=uuid.uuid4)
    name = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)
    description = Column(Text)
    created_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now)
    updated_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, nullable=False, default=True)
    deleted_datetime = Column(DateTime(timezone=True), nullable=True)
    map_zoom = Column(Integer(), nullable=False, default=5)
    map_center_lat = Column(Float(), nullable=False, default=1)
    map_center_lng = Column(Float(), nullable=False, default=1)
    documents = Column(Text)

    mapitems = relationship("MapItem", back_populates="project")

    def __repr__(self):
        return "<Project(name='{}')>".format(self.name)


__all__ = [
    "Project"
]
