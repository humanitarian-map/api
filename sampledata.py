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
            map_center_point=[23.4162, 25.6628]
        ),
        "mapitems": [
            MapItem(
                name="Item 1.1",
                description="This is the item 1.1",
                map_data={}
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
            map_center_point=[34.8021, 38.9968]
        ),
        "mapitems": [
            MapItem(
                name="Item 2.1",
                description="This is the item 2.1",
                map_data={}
            ),
            MapItem(
                name="Item 2.2",
                description="This is the item 2.2",
                map_data={}
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
