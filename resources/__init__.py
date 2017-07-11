import falcon


class CommonResource(object):
    def __init__(self, db=None):
        self.db = db

    def raise_not_found(self, *args, **kwargs):
        raise falcon.HTTPNotFound(*args, **kwargs)


class BaseCollection(CommonResource):
    pass


class BaseResource(CommonResource):
    pass
