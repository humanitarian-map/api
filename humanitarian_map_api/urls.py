"""humanitarian_map_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_nested import routers
from core import views


router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet, base_name="organizations")
router.register(r'users', views.UserViewSet, base_name="users")
router.register(r'projects', views.ProjectViewSet, base_name="projects")

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'map-items', views.MapItemViewSet, base_name='map-items')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(projects_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/login/', obtain_jwt_token),
    url(r'^api/auth/refresh/', refresh_jwt_token),
]
