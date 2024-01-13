#!/bin/usr/env python3
"""Basic auth class"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from base64 import b64decode


class BasicAuth(Auth):
    """This class inherits from Auth


    Args:
        Auth (b): this class inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[summary]

        Args:
            authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """[summary]

        Args:
            base64_authorization_header (str): [description]

        Returns:
            str: [description]
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """[summary]

        Args:
            decoded_base64_authorization_header (str): [description]

        Returns:
            (str, str): [description]
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """[summary]

        Args:
            user_email (str): [description]
            user_pwd (str): [description]

        Returns:
            TypeVar('User'): [description]
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user instance based on a cookie value"""
        header = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(base64)
        user, pwd = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user, pwd)
