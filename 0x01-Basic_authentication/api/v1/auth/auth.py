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
            - excluded_paths: A list of strings
            representing the excluded paths.

        Return:
            - False
        """
        if path is None or excluded_paths is None:
            return True

        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Authorization header.

        Args:
            - request: flask request object

        Return:
            - None
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user.

        Args:
            - request: flask request object

        Return:
            - None
        """
        
        return None
