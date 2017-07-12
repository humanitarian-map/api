#!/usr/bin/env python

import datetime
import random

from faker import Factory

from storage.database import manager as db
from storage.models.projects import Project
from storage.models.mapitems import MapItem
from utils.datetime import now


fake = Factory.create()


SAMPLE_CENTERS = (
    [35.10193406, 38.46862793],
    [25.89876194, 89.22546387],
    [49.32512199, 32.53051758],
    [40.3800284, 3.82324219],
    [-6.40264841, 34.67285156],
    [-21.37124437, 23.42285156],
    [2.98692739, -65.78613281],
    [-3.07469507, -59.89746094],
    [22.1059988, 21.70898438],
    [33.28461997, 54.05273438],
    [28.53627451, -103.84277344]
)

ICON_TYPES = (
    "warning",
    "camp",
    "checkpoint",
    "hospital",
    "idps",
    "mobile-clinic",
    "other"
)


def get_project(id):
    return Project(name="project Example {}".format(id),
                   slug="project-example-{}".format(id),
                   description=fake.paragraph(),
                   start_datetime=now() - datetime.timedelta(weeks=random.randint(2, 52)),
                   end_datetime=now() + datetime.timedelta(weeks=random.randint(12, 156)),
                   zoom=random.randint(5, 10),
                   center_point=random.choice(SAMPLE_CENTERS))


def get_cross(project):
    position = [random.uniform(project.center_point[0] - 3,
                               project.center_point[0] + 3),
                random.uniform(project.center_point[1] - 3,
                               project.center_point[1] + 3)]

    return MapItem(name=fake.sentences()[0],
                   project=project,
                   description=fake.paragraph(),
                   type="cross",
                   data={"position": position})


def get_point(project):
    position = [random.uniform(project.center_point[0] - 3,
                               project.center_point[0] + 3),
                random.uniform(project.center_point[1] - 3,
                               project.center_point[1] + 3)]

    return MapItem(name=fake.sentences()[0],
                   project=project,
                   description=fake.paragraph(),
                   type="point",
                   data={"icon": random.choice(ICON_TYPES),
                         "position": position})


def get_arrow(project):
    origin = [random.uniform(project.center_point[0] - 3,
                             project.center_point[0] + 3),
              random.uniform(project.center_point[1] - 3,
                             project.center_point[1] + 3)]
    dest = [random.uniform(origin[0] - 0.5,
                           origin[0] + 0.5),
            random.uniform(origin[1] - 0.5,
                           origin[1] + 0.5)]

    return MapItem(name=fake.sentences()[0],
                   project=project,
                   description=fake.paragraph(),
                   type="arrow",
                   data={"origin": origin,
                         "dest": dest})


def get_polygon(project):
    positions = [[random.uniform(project.center_point[0] - 3,
                                 project.center_point[0] + 3),
                  random.uniform(project.center_point[1] - 3,
                                 project.center_point[1] + 3)]]

    for i in range(1, random.randint(4, 7)):
        last = positions[len(positions) - 1]
        positions.append([random.uniform(last[0] - 3,
                                         last[0] + 3),
                          random.uniform(last[1] - 3,
                                         last[1] + 3)])

    return MapItem(name=fake.sentences()[0],
                   project=project,
                   description=fake.paragraph(),
                   type="polygon",
                   data={"positions": positions})


MAPITEM_GENERATORS = (
    get_point,
    get_cross,
    get_arrow,
    get_polygon
)


if __name__ == "__main__":
    print("Drop DB")
    db.delete()
    print("Create DB")
    db.setup()

    for id in range(1, 100):
        project = get_project(id)

        db.session.add(project)
        db.session.flush()
        print("> Create project:", project)

        for i in range(4, random.randint(4, 20)):
            item = random.choice(MAPITEM_GENERATORS)(project)

            db.session.add(item)
            db.session.flush()
            print("    - Create map item:", item)

    db.session.commit()
