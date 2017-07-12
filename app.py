#!/usr/bin/env python
import falcon
from falcon_cors import CORS
from falconjsonio import middleware as falconjsonio_middleware

from resources.mapitems import MapItemsCollection, MapItemResource
from resources.projects import ProjectsCollection, ProjectResource
import settings
from storage.database import manager as db


# Initialize the database
db.setup()


# CORS
cors = CORS(allow_all_origins=settings.ALLOW_ALL_ORIGINS,
            allow_origins_list=settings.ALLOW_ORIGINS)


# Middlewares
middlewares = [
    cors.middleware,
    falconjsonio_middleware.RequireJSON(),
    falconjsonio_middleware.JSONTranslator(),
]


# Create the app
api = application = application = falcon.API(middleware=middlewares)


# Create Resources
api.add_route("/api/projects", ProjectsCollection(db=db))
api.add_route("/api/projects/{slug}", ProjectResource(db=db))
api.add_route("/api/mapitems", MapItemsCollection(db=db))
api.add_route("/api/mapitems/{id}", MapItemResource(db=db))
