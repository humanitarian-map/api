import falcon

from utils import json


class ProjectsResource(object):
    def on_get(self, req, res):
        body = {
            'text': 'ProjectsResource GET tests'
        }

        res.status = falcon.HTTP_200
        res.body = json.dumps(body)
