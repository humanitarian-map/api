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
            zoom=5,
            center_point=[23.4162, 25.6628]
        ),
        "mapitems": [
            MapItem(
                name="Item 1.1",
                description="This is the item 1.1",
                type="arrow",
                data={"origin": [27.705, 37.80], "dest": [28.305, 37.29]}
            ),
            MapItem(
                name="Item 1.2",
                description="This is the item 1.2",
                type="polygon",
                data={"positions": [[28.705, 37.80], [28.705, 38.80], [29.305, 37.29]]}
            ),
        ]
    },
    # Project 2
    {
        "project": Project(
            name="project Example 2",
            slug="project-example-2",
            description="This is an example project.",
            zoom=5,
            center_point=[34.8021, 38.9968]
        ),
        "mapitems": [
            MapItem(
                name="Item 2.1",
                description="This is the item 2.1",
                type="point",
                data={"icon": "camp", "position": [29.505, 39.09]}
            ),
            MapItem(
                name="Item 2.2",
                description="This is the item 2.2",
                type="cross",
                data={"position": [28.505, 37.09]}
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
