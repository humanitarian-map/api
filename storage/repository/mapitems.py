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


def update_mapitem(session, slug, id, name, type, data, description):
    obj = get_mapitem_by_id(session, slug, id)

    obj.name = name
    obj.type = type
    obj.data = data
    obj.description = description

    session.add(obj)
    session.flush()

    return obj


def delete_mapitem_by_id(session, slug, id):
    obj = get_mapitem_by_id(session, slug, id)

    if not obj:
        return False

    obj.is_active = False

    session.add(obj)
    session.flush()
    return True


__all__ = [
    "list_mapitems",
    "get_mapitem_by_id",
    "create_mapitem",
    "update_mapitem",
    "delete_mapitem_by_id"
]
