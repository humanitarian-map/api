from django.contrib import admin

from .models import Organization, OrganizationMember, Project, ProjectMember, MapItem


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "is_public"]
    list_filter = ["is_public"]


admin.site.register(Organization, OrganizationAdmin)


class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ["user", "organization", "role"]
    list_filter = ["organization", "role"]


admin.site.register(OrganizationMember, OrganizationMemberAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "organization", "is_public"]
    list_filter = ["organization", "is_public"]


admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(admin.ModelAdmin):
    def organization(self, obj):
        return obj.project.organization.name

    def project_name(self, obj):
        return obj.project.name

    list_display = ["user", "organization", "project_name", "role"]
    list_filter = ["role", "project__organization"]


admin.site.register(ProjectMember, ProjectMemberAdmin)


class MapItemAdmin(admin.ModelAdmin):
    list_display = ["slug", "is_active", "type", "project"]
    list_filter = ["is_active", "type", "project__name", "project__organization"]


admin.site.register(MapItem, MapItemAdmin)
