#!/usr/bin/env python
import falcon
from falcon_cors import CORS


from resources.mapitems import MapItemsCollection, MapItemResource
from resources.projects import ProjectsCollection, ProjectResource

import settings

from storage.database import manager as db


# Initialize the database
db.setup()


# Middlewares
cors = CORS(allow_origins_list=settings.ALLOW_ORIGINS)

middlewares = [
    cors.middleware
]


# Create the app
api = application = application = falcon.API(middleware=middlewares)


# Create Resources
api.add_route("/api/projects", ProjectsCollection(db=db))
api.add_route("/api/projects/{slug}", ProjectResource(db=db))
api.add_route("/api/mapitems", MapItemsCollection(db=db))
api.add_route("/api/mapitems/{id}", MapItemResource(db=db))
