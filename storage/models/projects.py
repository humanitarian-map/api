import uuid

from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, Text
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

    start_date = Column(Date(), nullable=True)
    end_date = Column(Date(), nullable=True)

    zoom = Column(Integer(), nullable=False, default=5)
    center_point = Column(ARRAY(Float, dimensions=1), nullable=False, default=1)

    created_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now)
    updated_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, nullable=False, default=True)
    deleted_datetime = Column(DateTime(timezone=True), nullable=True)

    organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'))
    organization = relationship("Organization", back_populates="projects")

    mapitems = relationship("MapItem", back_populates="project",
                            primaryjoin="and_(Project.id==MapItem.project_id, "
                                        " MapItem.is_active==True)")

    __serialized_fields__ = [
        "id",
        "name",
        "slug",
        "description",
        "start_date",
        "end_date",
        "zoom",
        "center_point",
        "organization",
        "mapitems"
    ]

    def __repr__(self):
        return "<Project(name='{}')>".format(self.name)


__all__ = [
    "Project"
]
