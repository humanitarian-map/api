#!/usr/bin/env python
import falcon

from resources.mapitems import MapItemsResource
from resources.projects import ProjectsResource

from storage.database import init_db

# Initialize the database
init_db()


# Create the app
api = application = application = falcon.API()


# Create Resources
api.add_route('/projects', ProjectsResource())
api.add_route('/mapitems', MapItemsResource())