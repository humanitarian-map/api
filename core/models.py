from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from slugify import slugify
import uuid


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False)
    slug = models.TextField(null=False, blank=True, unique=True)
    image = models.TextField(null=True)
    web = models.TextField(null=True)
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField()

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

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

    class Meta:
        ordering = ["name"]


ORGANIZATION_ROLES_CHOICES = [
    ('admin', 'Admin'),
    ('member', 'Member'),
]


class OrganizationMember(models.Model):
    user = models.ForeignKey('auth.User')
    organization = models.ForeignKey(Organization, related_name="members")
    role = models.CharField(max_length=20, choices=ORGANIZATION_ROLES_CHOICES)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.TextField(null=False)
    slug = models.TextField(null=False, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    zoom = models.IntegerField(null=False, default=5)
    center_point = ArrayField(models.FloatField(), 2, null=False)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(null=False, default=True)
    deleted_datetime = models.DateTimeField(null=True)

    organization = models.ForeignKey("Organization", related_name="projects")
    is_public = models.BooleanField()

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

    def __str__(self):
        return "{} - {}".format(self.organization, self.name)

    class Meta:
        ordering = ["name"]


PROJECT_ROLES_CHOICES = [
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('member', 'Member'),
]


class ProjectMember(models.Model):
    user = models.ForeignKey('auth.User')
    project = models.ForeignKey(Project, related_name="members")
    role = models.CharField(max_length=20, choices=PROJECT_ROLES_CHOICES)


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
    slug = models.TextField(null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(null=False, default=True)
    deleted_datetime = models.DateTimeField(null=True)
    type = models.TextField(choices=ITEM_TYPES_CHOICES, null=False)
    data = JSONField(null=False, default={})

    project = models.ForeignKey("Project", related_name="mapitems")

    def __str__(self):
        return "{} ({})".format(self.name, self.type)

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

    class Meta:
        ordering = ["id"]
