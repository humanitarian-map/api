#!/usr/bin/env python
import falcon

from resources.mapitems import MapItemsCollection, MapItemResource
from resources.projects import ProjectsCollection, ProjectResource

from storage.database import manager as db


# Initialize the database
db.setup()


# Create the app
api = application = application = falcon.API()


# Create Resources
api.add_route("/api/projects", ProjectsCollection(db=db))
api.add_route("/api/projects/{slug}", ProjectResource(db=db))
api.add_route("/api/mapitems", MapItemsCollection(db=db))
api.add_route("/api/mapitems/{id}", MapItemResource(db=db))
