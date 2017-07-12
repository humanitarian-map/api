import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
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
    zoom = Column(Integer(), nullable=False, default=5)
    center_point = Column(ARRAY(Float, dimensions=1), nullable=False, default=1)

    mapitems = relationship("MapItem", back_populates="project")

    def __repr__(self):
        return "<Project(name='{}')>".format(self.name)


__all__ = [
    "Project"
]
