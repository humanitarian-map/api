from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status

from core.base.api.mixins import NestedViewSetMixin
from core.models import Project, MapItem, Organization
from core.serializers import OrganizationSerializer, ProjectSerializer, MapItemSerializer, UserSerializer

from django.contrib.auth.models import User
from django.db.models import Q

from .service import list_project_documents


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            return Organization.objects.filter(Q(is_public=True) | Q(members__id=user.id))
        return Organization.objects.filter(is_public=True)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    lookup_field = "slug"

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            # TODO: Review the organization filtering
            return Project.objects.filter(
                Q(is_public=True) |
                Q(members__id=user.id) |
                Q(organization__members__id=user.id, organization__members__role="admin")
            )
        return Project.objects.filter(is_public=True)

    @detail_route(methods=["get"])
    def documents(self, request, slug=None):
        result = list_project_documents(slug)
        return Response(result)


class MapItemViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = MapItemSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            # TODO: Review the organization filtering
            return (MapItem.objects.filter(
                Q(project__is_public=True) |
                Q(project__members__id=user.id) |
                Q(project__organization__members__id=user.id, project__organization__members__role="admin")
            ))
        return MapItem.objects.filter(project__is_public=True)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=["GET"])
    def me(self, request):
        if request.user.is_authenticated():
            return Response(UserSerializer(request.user).data)
        return Response("", status=status.HTTP_401_UNAUTHORIZED)
