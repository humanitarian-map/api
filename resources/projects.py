import falcon

from resources import BaseCollection, BaseResource
from storage import repository
from utils import json


class ProjectsCollection(BaseCollection):
    def on_get(self, req, res):
        body = repository.list_projects(self.db.session)

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)


class ProjectResource(BaseResource):
    def on_get(self, req, res, slug):
        project = repository.get_project_by_slug(self.db.session, slug)
        if not project:
            self.raise_not_found(name="Project not found")

        body = project.as_dict()
        body["mapitems"] = [mi for mi in project.mapitems]

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)
