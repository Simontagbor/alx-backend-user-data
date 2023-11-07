"""
defines a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class

    Attributes:
        - allowed: list of strings
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth

        Args:
            - path: string
            - excluded_paths: list of strings

        Return:
            - True if path is not in excluded_paths
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header

        Args:
            - request: flask request object

        Return:
            - None or request.headers.get('Authorization')
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user

        Args:
            - request: flask request object

        Return:
            - None
        """
        return None
