from storage.models.mapitems import MapItem


def list_mapitems(session, is_active=True):
    return session.query(MapItem).filter_by(is_active=is_active).all()


def get_mapitem_by_id(session, id):
    return session.query(MapItem).filter_by(id=id).one_or_none()


def create_mapitem(session, name, project_id, type, data, description=None):
    obj = MapItem(name=name,
                  project_id=project_id,
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
