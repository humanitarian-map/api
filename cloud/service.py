import owncloud
import settings
import os.path


def on_create_project(project_slug, creator):
    oc = owncloud.Client(settings.OWNCLOUD_HOST)
    oc.login(settings.OWNCLOUD_USERNAME, settings.OWNCLOUD_PASSWORD)
    try:
        oc.mkdir(project_slug)
    except Exception:
        pass

    try:
        oc.create_group(project_slug)
    except Exception:
        pass

    try:
        oc.add_user_to_group(creator, project_slug)
    except Exception:
        pass

    try:
        oc.share_file_with_group(project_slug, project_slug, perms=oc.OCS_PERMISSION_ALL)
    except Exception:
        pass


def on_create_point(project_slug, point_name):
    oc = owncloud.Client(settings.OWNCLOUD_HOST)
    oc.login(settings.OWNCLOUD_USERNAME, settings.OWNCLOUD_PASSWORD)
    oc.mkdir(os.path.join(project_slug, point_name))


def on_add_user_to_project(project_slug, username):
    oc = owncloud.Client(settings.OWNCLOUD_HOST)
    oc.login(settings.OWNCLOUD_USERNAME, settings.OWNCLOUD_PASSWORD)
    oc.add_user_to_group(username, project_slug)


def on_remove_user_from_project(project_slug, username):
    oc = owncloud.Client(settings.OWNCLOUD_HOST)
    oc.login(settings.OWNCLOUD_USERNAME, settings.OWNCLOUD_PASSWORD)
    oc.remove_user_from_group(username, project_slug)


def get_project_folder_url(project_slug):
    return "{}/index.php/apps/files/?dir=/{}".format(settings.OWNCLOUD_HOST, project_slug)


def get_point_folder_url(project_slug, point_name):
    return "{}/index.php/apps/files/?dir=/{}/{}".format(settings.OWNCLOUD_HOST, project_slug, point_name)
