from storage.models.mapitems import MapItem
from storage.models.projects import Project


def list_mapitems(session, slug, is_active=True):
    return session.query(MapItem).filter(MapItem.is_active == is_active,
                                         Project.slug == slug).all()


def get_mapitem_by_id(session, slug, id):
    return session.query(MapItem).filter(MapItem.id == id,
                                         Project.slug == slug).one_or_none()


def create_mapitem(session, project, name, type, data, description=None):
    obj = MapItem(name=name,
                  project=project,
                  type=type,
                  data=data,
                  description=description)
    session.add(obj)
    session.flush()
    return obj


__all__ = [
    "list_mapitems",
    "get_mapitem_by_id",
    "create_mapitem"
]
