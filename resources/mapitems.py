import falcon
from falconjsonio.schema import request_schema

from resources import BaseResource, BaseCollection
import schemas
from storage import repository
from utils import json


class MapItemsCollection(BaseCollection):
    def on_get(self, req, res):
        body = repository.list_mapitems(self.db.session)

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)

    @request_schema(schemas.mapitems.create)
    def on_post(self, req, res):
        data = req.context["doc"]
        body = repository.create_mapitem(self.db.session, **data)

        res.status = falcon.HTTP_201
        res.body = json.dumps(body)


class MapItemResource(BaseResource):
    def on_get(self, req, res, id):
        body = repository.get_mapitem_by_id(self.db.session, id)

        if not body:
            self.raise_not_found(name="MapItem not found")

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)
