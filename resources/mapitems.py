import falcon
from falconjsonio.schema import request_schema

from resources import BaseResource, BaseCollection
import schemas
from storage import repository
from utils import json


class MapItemsCollection(BaseCollection):
    def on_get(self, req, res, slug):
        project = repository.get_project_by_slug(self.db.session, slug)

        if not project:
            self.raise_not_found(title="Project not found")

        body = repository.list_mapitems(self.db.session, slug)

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)

    @request_schema(schemas.mapitems.create)
    def on_post(self, req, res, slug):
        project = repository.get_project_by_slug(self.db.session, slug)

        if not project:
            self.raise_not_found(title="Project not found")

        data = req.context["doc"]
        body = repository.create_mapitem(self.db.session, project, **data)
        self.db.session.commit()

        res.status = falcon.HTTP_201
        res.body = json.dumps(body)


class MapItemResource(BaseResource):
    def on_get(self, req, res, slug, id):
        body = repository.get_mapitem_by_id(self.db.session, slug, id)

        if not body:
            self.raise_not_found(title="MapItem not found")

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)

    @request_schema(schemas.mapitems.update)
    def on_put(self, req, res, slug, id):
        data = req.context["doc"]
        body = repository.update_mapitem(self.db.session, slug, id, **data)

        if not body:
            self.raise_not_found(title="MapItem not found")

        self.db.session.commit()

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)

    def on_delete(self, req, res, slug, id):
        delete = repository.delete_mapitem_by_id(self.db.session, slug, id)

        if delete:
            self.db.session.commit()
            res.status = falcon.HTTP_204
        else:
            self.raise_not_found(title="MapItem not found")
