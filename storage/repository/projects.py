from storage.models.projects import Project


def list_projects(session, is_active=True):
    return (session.query(Project).join(Project.organization)
                                  .filter(Project.is_active == is_active)
                                  .all())


def get_project_by_slug(session, slug):
    return (session.query(Project).join(Project.mapitems, Project.organization)
                                  .filter(Project.slug == slug)
                                  .one_or_none())


__all__ = [
    "list_projects",
    "get_project_by_slug"
]
