from .service import list_project_documents
from core.models import Project, MapItem, Organization
from rest_framework import viewsets
from core.serializers import OrganizationSerializer, ProjectSerializer, MapItemSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"

    @detail_route(methods=["get"])
    def documents(self, request, slug=None):
        result = list_project_documents(slug)
        return Response(result)


class MapItemViewSet(viewsets.ModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = MapItemSerializer
