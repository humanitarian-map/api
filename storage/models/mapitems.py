import enum
import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ENUM, JSONB, UUID
from sqlalchemy.orm import relationship


from storage.database import manager
from utils import datetime
from cloud.service import get_point_folder_url


class ItemTypes(enum.Enum):
    cross = "cross"
    point = "point"
    icon = "icon"
    arrow = "arrow"
    polygon = "polygon"


class MapItem(manager.Base):
    __tablename__ = "mapitem"
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
    type = Column(ENUM(ItemTypes, name="item_types"), nullable=False)
    data = Column(JSONB(), nullable=False, default={})

    project_id = Column(UUID(as_uuid=True), ForeignKey('project.id'))
    project = relationship("Project", back_populates="mapitems")

    __serialized_fields__ = [
        "id",
        "name",
        "slug",
        "description",
        "is_active",
        "type",
        "data",
        "documents_url",
    ]

    def __repr__(self):
        return "<MapItem(type={}, name='{}')>".format(self.type, self.name)

    @property
    def documents_url(self):
        if self.type == ItemTypes.point:
            return get_point_folder_url(self.project.slug, self.slug)
        return None


__all__ = [
    "MapItem"
]
