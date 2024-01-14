#!/usr/bin/env python3
"""
defines a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv
import fnmatch


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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
    
        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

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
