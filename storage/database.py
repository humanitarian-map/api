from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import settings


class Base(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class DBManager(object):
    def __init__(self):
        self.engine = create_engine(URL(**settings.DB["url"]),
                                    **settings.DB["extra_settings"])
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=self.engine))
        self.Base = declarative_base(cls=Base)
        self.Base.query = self.db_session.query_property()

    @property
    def session(self):
        return self.db_session()

    def setup(self):
        # import all modules here that might define models so that
        # they will be registered properly on the metadata.
        from .models import (Project,   # noqa
                             MapItem)   # noqa

        try:
            self.Base.metadata.create_all(bind=self.engine)
        except Exception as e:
            print('Could not initialize DB: {}'.format(e))

    def delete(self):
        self.Base.metadata.drop_all(bind=self.engine)


manager = DBManager()
