import uuid

from sqlalchemy import Column, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from storage.database import manager
from utils import datetime


class Organization(manager.Base):
    __tablename__ = "organization"
    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True,
                default=uuid.uuid4)
    name = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)
    image = Column(Text, nullable=True)
    web = Column(Text, nullable=True)
    description = Column(Text)

    created_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now)
    updated_datetime = Column(DateTime(timezone=True), nullable=False,
                              default=datetime.now, onupdate=datetime.now)

    projects = relationship("Project", back_populates="organization")

    __serialized_fields__ = [
        "id",
        "name",
        "slug",
        "image",
        "web",
        "description",
    ]

    def __repr__(self):
        return "<Organization(name='{}')>".format(self.name)


__all__ = [
    "Organization"
]
