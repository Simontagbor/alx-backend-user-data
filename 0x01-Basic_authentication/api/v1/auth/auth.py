#!/usr/bin/env python3
"""
defines a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Handles authentication for users"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth.

        Args:
            - path: A string representing the path.
            - excluded_paths: A list of strings representing the excluded paths.

        Return:
            - False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header.

        Args:
            - request: flask request object

        Return:
            - None
        """
        return request.headers.get('Authorization') if request else None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.

        Args:
            - request: flask request object

        Return:
            - None
        """
        return None
