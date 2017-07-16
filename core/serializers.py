from core.models import Project, MapItem, Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name", "slug", "image", "web", "description",
                  "created_datetime", "updated_datetime")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")


class MapItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapItem
        fields = ("name", "slug", "description", "type", "data",
                  "created_datetime", "updated_datetime")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")


class ProjectSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=False)
    mapitems = MapItemSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "name", "slug", "description", "start_date",
                  "end_date", "zoom", "center_point", "organization",
                  "mapitems", "created_datetime", "updated_datetime")
        read_only_fiels = ("created_datetime", "updated_datetime", "slug")
        lookup_field = "slug"
