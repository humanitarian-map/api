from storage.models.projects import Project


def list_projects(session, is_active=True):
    return (session.query(Project).join(Project.organization)
                                  .filter(Project.is_active == is_active)
                                  .order_by(Project.name)
                                  .all())


def get_project_by_slug(session, slug):
    return (session.query(Project).join(Project.mapitems, Project.organization)
                                  .filter(Project.slug == slug)
                                  .one_or_none())


def update_project(session, slug, name, description, start_date, end_date, zoom, center_point, **kwargs):
    obj = get_project_by_slug(session, slug)

    obj.name = name
    obj.description = description
    obj.start_date = start_date
    obj.end_date = end_date
    obj.zoom = zoom
    obj.center_point = center_point

    session.add(obj)
    session.flush()

    return obj


__all__ = [
    "list_projects",
    "get_project_by_slug",
    "update_project"
]
