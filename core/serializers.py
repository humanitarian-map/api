from core.models import Project, MapItem, Organization
from rest_framework import serializers
from .service import get_project_folder_url, get_point_folder_url
from django.contrib.auth.models import User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("id", "name", "slug", "image", "web", "description",
                  "created_datetime", "updated_datetime")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")


class MapItemSerializer(serializers.ModelSerializer):
    documents_url = serializers.SerializerMethodField()

    def get_documents_url(self, obj):
        if obj.type == "point":
            return get_point_folder_url(obj.project.slug, obj.slug)
        return None

    class Meta:
        model = MapItem
        fields = ("id", "name", "slug", "description", "type", "data",
                  "created_datetime", "updated_datetime", "documents_url",
                  "project")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")


class ProjectSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=False)
    mapitems = MapItemSerializer(many=True)
    documents_url = serializers.SerializerMethodField()

    def get_documents_url(self, obj):
        return get_project_folder_url(obj.slug)

    class Meta:
        model = Project
        fields = ("id", "name", "slug", "description", "start_date",
                  "end_date", "zoom", "center_point", "organization",
                  "mapitems", "created_datetime", "updated_datetime",
                  "documents_url")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")
        lookup_field = "slug"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email")
