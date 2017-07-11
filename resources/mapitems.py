import falcon

from utils import json


class MapItemsResource(object):
    def on_get(self, req, res):
        body = {
            'text': 'MapItemsResource GET tests'
        }

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)
