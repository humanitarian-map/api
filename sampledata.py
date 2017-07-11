#!/usr/bin/env python
from storage.database import manager as db
from storage.models.projects import Project
from storage.models.mapitems import MapItem


sample_data = [
    # Project 1
    {
        "project": Project(
            name="project Example 1",
            slug="project-example-1",
            description="This is an example project.",
            map_zoom=5,
            map_center_lat=23.4162,
            map_center_lng=25.6628,
            documents="http://example1.com",
        ),
        "mapitems": [
            MapItem(
                name="Item 1.1",
                description="This is the item 1.1",
                map_data={},
                documents="http://example11.com",
            ),
        ]
    },
    # Project 2
    {
        "project": Project(
            name="project Example 2",
            slug="project-example-2",
            description="This is an example project.",
            map_zoom=5,
            map_center_lat=34.8021,
            map_center_lng=38.9968,
            documents="http://example2.com",
        ),
        "mapitems": [
            MapItem(
                name="Item 2.1",
                description="This is the item 2.1",
                map_data={},
                documents="http://example21.com",
            ),
            MapItem(
                name="Item 2.2",
                description="This is the item 2.2",
                map_data={},
                documents="http://example22.com",
            ),
        ]
    },
]

if __name__ == "__main__":
    print("Drop DB")
    db.delete()
    print("Create DB")
    db.setup()

    for data in sample_data:
        project = data["project"]
        mapitems = data["mapitems"]

        db.session.add(project)
        db.session.flush()
        print("> Create project:", project)
        for item in mapitems:
            item.project = project
            db.session.add(item)
            db.session.flush()
            print("    - Create map item:", item)

    db.session.commit()
