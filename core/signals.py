from django.db.models.signals import post_save
from .models import Project, MapItem
from .service import on_create_project, on_create_point


def project_creation(sender, instance, created):
    if created:
        on_create_project(instance.slug)


def point_creation(sender, instance, created):
    if created and instance.type == "point":
        on_create_point(instance.project.slug, instance.slug)


def connect_signals():
    post_save.connect(project_creation, sender=Project)
    post_save.connect(point_creation, sender=MapItem)
