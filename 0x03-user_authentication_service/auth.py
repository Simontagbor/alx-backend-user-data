#!/usr/bin/env python3
"""
Module to define authentication class
"""
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hashes a password with bcrypt

    Args:
        password(str) - password to be hashed
    Return:
        hashed_password(bytes)
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """Generates a uuid and retuns a string representation of uuid"""
    random_id = uuid4()
    return str(random_id)


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user

        Args:
            email(str)
            password(str)

        Return:
                New user instance
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"{email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate the login of the user

        Args:
            email(str)
            password(str)

        Return:
            Bool
        """
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')
            hashed_password = user.hashed_password
            if bcrypt.checkpw(password, hashed_password):
                return True
            return False
        except NoResultFound:
            return False
