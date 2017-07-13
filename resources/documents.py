import falcon

from cloud import service as cloud_service
from resources import BaseCollection
from storage import repository
from utils import json


class DocumentsCollection(BaseCollection):
    def on_get(self, req, res, slug):
        project = repository.get_project_by_slug(self.db.session, slug)
        if not project:
            self.raise_not_found(title="Project not found")

        body = cloud_service.list_project_documents(slug)

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)
