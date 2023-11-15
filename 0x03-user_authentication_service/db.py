#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """
    self._engine = create_engine("sqlite:///a.db", echo=True)
    Base.metadata.drop_all(self._engine)
    Base.metadata.create_all(self._engine)
    
    self.__session = None

    @property
    def _session(self) -> Session:
        """
        memoize session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email, hashed_password):
        """ 
        returns a User object
        """


