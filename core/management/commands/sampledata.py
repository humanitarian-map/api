from django.core.management.base import BaseCommand

import datetime
import random

from faker import Factory

# from cloud import service as cloud_service
from core.models import Organization, Project, MapItem


####################################################################
## Sampledata
####################################################################

SEED = 1234567890


SAMPLE_ORGANIZATIONS = [
    {
        "name": "Medicos Del Mundo",
        "image": "https://www.medicosdelmundo.org/sites/default/files/medicosdelmundo.png",
        "web": "https://www.medicosdelmundo.org/",
        "description": "Médicos del Mundo es una asociación independiente que trabaja para hacer efectivo el derecho "
                       "a la salud para todas las personas, especialmente para las poblaciones vulnerables, excluidas "
                       "o víctimas de catástrofes naturales, hambrunas, enfermedades, conflictos armados o violencia "
                       "política. Nuestros proyectos se realizan tanto en España como en más de 20 países de Asia, "
                       "América, África, Oriente Medio y Europa. Las personas voluntarias y profesionales que forman "
                       "parte de nuestra organización tienen como principal misión trabajar para lograr cumplimiento "
                       "del derecho fundamental a la salud y el disfrute de una vida digna para cualquier persona."
    },
    {
        "name": "Save The Children",
        "image": "http://www.savethechildren.org.uk/sites/all/themes/freshlime/ui/stc_logo.png",
        "web": "http://www.savethechildren.net",
        "description": "Save the Children believes every child deserves a future. Around the world, we give children "
                       "a healthy start in life, the opportunity to learn and protection from harm. We do whatever it "
                       "takes for children – every day and in times of crisis – transforming their lives and the "
                       "future we share."
    },
    {
        "name": "Oxfam International",
        "image": "http://static.oxfamamerica.org.s3.amazonaws.com/images/logos/oxfam_logo_vertical_green_rgb.png",
        "web": ",https://www.oxfam.org/",
        "description": "Oxfam is an international confederation of charitable organizations focused on the "
                       "alleviation of global poverty. Oxfam's programmes address the structural causes of poverty "
                       "and related injustice and work primarily through local accountable organizations, seeking "
                       "to enhance their effectiveness. Oxfam's stated goal is to help people directly when local "
                       "capacity is insufficient or inappropriate for Oxfam's purposes, and to assist in the "
                       "development of structures which directly benefit people facing the realities of poverty and "
                       "injustice."
    },
    {
        "name": "World Wide Fund for Nature",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/24/WWF_logo.svg/263px-WWF_logo.svg.png",
        "web": "https://www.worldwildlife.org/",
        "description": "For 50 years, WWF has been protecting the future of nature. The world’s leading conservation "
                       "organization, WWF works in 100 countries and is supported by more than one million members in "
                       "the United States and close to five million globally. WWF's unique way of working combines "
                       "global reach with a foundation in science, involves action at every level from local to "
                       "global, and ensures the delivery of innovative solutions that meet the needs of both people "
                       "and nature."
    }
]


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


def get_organization(name, image, web, description):
    return Organization.objects.create(
        name=name,
        image=image,
        web=web,
        description=description
    )


def get_project(organization, id):
    name = fake.sentence()

    return Project.objects.create(
        name=name,
        organization=organization,
        description=fake.paragraph(),
        start_date=datetime.datetime.now().date() - datetime.timedelta(weeks=random.randint(2, 52)),
        end_date=datetime.datetime.now().date() + datetime.timedelta(weeks=random.randint(12, 156)),
        zoom=random.randint(4, 7),
        center_point=random.choice(SAMPLE_CENTERS)
    )


def get_cross(project):
    name = fake.sentence()
    position = [random.uniform(project.center_point[0] - 3,
                               project.center_point[0] + 3),
                random.uniform(project.center_point[1] - 3,
                               project.center_point[1] + 3)]

    return MapItem.objects.create(
        name=name,
        project=project,
        description=fake.paragraph(),
        type="cross",
        data={"position": position}
    )


def get_point(project):
    name = fake.sentence()
    position = [random.uniform(project.center_point[0] - 3,
                               project.center_point[0] + 3),
                random.uniform(project.center_point[1] - 3,
                               project.center_point[1] + 3)]

    return MapItem.objects.create(
        name=name,
        project=project,
        description=fake.paragraph(),
        type="point",
        data={"icon": random.choice(ICON_TYPES),
              "position": position}
    )


def get_arrow(project):
    name = fake.sentence()
    origin = [random.uniform(project.center_point[0] - 3,
                             project.center_point[0] + 3),
              random.uniform(project.center_point[1] - 3,
                             project.center_point[1] + 3)]
    dest = [random.uniform(origin[0] - 0.5,
                           origin[0] + 0.5),
            random.uniform(origin[1] - 0.5,
                           origin[1] + 0.5)]

    return MapItem.objects.create(
        name=name,
        project=project,
        description=fake.paragraph(),
        type="arrow",
        data={"origin": origin,
              "dest": dest}
    )


def get_polygon(project):
    name = fake.sentence()
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

    return MapItem.objects.create(
        name=name,
        project=project,
        description=fake.paragraph(),
        type="polygon",
        data={"positions": positions}
    )


MAPITEM_GENERATORS = (
    get_point,
    get_cross,
    get_arrow,
    get_polygon
)


random.seed(SEED)
fake = Factory.create()
fake.seed(SEED)


class Command(BaseCommand):
    help = 'Generate sample data'

    def handle(self, *args, **options):
        organizations = []
        for data in SAMPLE_ORGANIZATIONS:
            org = get_organization(**data)
            print(". Create organization: {}".format(org))
            organizations.append(org)

        for id in range(1, 31):
            project = get_project(random.choice(organizations), id)
            # cloud_service.on_create_project(project.slug)
            print("> Create project: {}".format(project))

            for i in range(1, random.randint(4, 20)):
                item = random.choice(MAPITEM_GENERATORS)(project)
                # if item.type == "point":
                #     cloud_service.on_create_point(project.slug, item.name)
                print("    - Create map item: {}".format(item))
