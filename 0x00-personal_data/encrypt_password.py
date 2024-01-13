#!/usr/bin/env python3
"""This module contains the hash_password function."""

import bcrypt


def hash_password(password: str) -> bytes:
    """This function returns a salted,
      hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """This function validates that the provided
      password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
