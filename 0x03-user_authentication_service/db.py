#!/usr/bin/env python3
"""DB module for defining database interaction with sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Type

from user import Base, User


class DB:
    """DB class for models
    
    Attributes: _session
                add_user()
    """
    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def add_user(self, email: str, hashed_password: str) -> Type[User]:
        """
        Adds a User Instance to Database

        Args:
            email(string) - email of user
            hashed_password(string) - password of user
        Return:
            User instance(object)
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        return new_user
