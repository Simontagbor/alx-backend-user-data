#!/usr/bin/env python3
"""
Defines a model for user
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# define user based on base


class User(Base):
    """
    A simple class that creates users

    Attributes:
                id(int)
                email(str)
                hashed_password(str)
                session_id(str)
                reset_token(str)
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=True)
