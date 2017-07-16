from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from slugify import slugify
import uuid


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    slug = models.TextField(null=False, unique=True)
    image = models.TextField(null=True)
    web = models.TextField(null=True)
    description = models.TextField(null=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "<Organization(name='{}')>".format(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)  # change the attibute to the field that would be used as a slug
            new_slug = slug
            count = 0
            while Organization.objects.filter(slug=new_slug).exclude(id=self.id).count() > 0:
                count += 1
                new_slug = '{slug}-{count}'.format(slug=slug, count=count)

            self.slug = new_slug
        return super().save(*args, **kwargs)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.TextField(null=False)
    slug = models.TextField(null=False, unique=True)
    description = models.TextField(null=True)

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    zoom = models.IntegerField(null=False, default=5)
    center_point = ArrayField(models.FloatField(), 2, null=False)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(null=False, default=True)
    deleted_datetime = models.DateTimeField(null=True)

    organization = models.ForeignKey("Organization", related_name="projects")

    # @property
    # def documents_url(self):
    #     return get_project_folder_url(self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)  # change the attibute to the field that would be used as a slug
            new_slug = slug
            count = 0
            while Project.objects.filter(slug=new_slug).exclude(id=self.id).count() > 0:
                count += 1
                new_slug = '{slug}-{count}'.format(slug=slug, count=count)

            self.slug = new_slug
        return super().save(*args, **kwargs)

    def __unicode__(self):
        return "<Project(name='{}')>".format(self.name)


ITEM_TYPES_CHOICES = [
    ("cross", "Cross"),
    ("point", "Point"),
    ("icon", "Icon"),
    ("arrow", "Arrow"),
    ("polygon", "Polygon")
]


class MapItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.TextField(null=False)
    slug = models.TextField(null=False)
    description = models.TextField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(null=False, default=True)
    deleted_datetime = models.DateTimeField(null=True)
    type = models.TextField(choices=ITEM_TYPES_CHOICES, null=False)
    data = JSONField(null=False, default={})

    project = models.ForeignKey("Project", related_name="mapitems")

    def __unicode__(self):
        return "<MapItem(type={}, name='{}')>".format(self.type, self.name)

    # @property
    # def documents_url(self):
    #     if self.type == ItemTypes.point:
    #         return get_point_folder_url(self.project.slug, self.slug)
    #     return None

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)  # change the attibute to the field that would be used as a slug
            new_slug = slug
            count = 0
            while MapItem.objects.filter(slug=new_slug).exclude(id=self.id).count() > 0:
                count += 1
                new_slug = '{slug}-{count}'.format(slug=slug, count=count)

            self.slug = new_slug
        return super().save(*args, **kwargs)
