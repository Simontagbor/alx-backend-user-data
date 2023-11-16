#!/usr/bin/env python3
"""
Module to define authentication class
"""
from user import User
from db import DB
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


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
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

    def register_user(self, user) -> User:
        """Registers a user"""
        pass
