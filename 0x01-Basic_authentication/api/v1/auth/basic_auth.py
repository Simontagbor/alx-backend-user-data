#!/usr/bin/env python3
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
            return None
        if ":" not in decoded_base64_authorization_header:
            return None
        user_credentials = decoded_base64_authorization_header.split(":", 1)
        return user_credentials

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
        """Retrieve the User instance for a request."""
        if request is None:
            return None

        authorization_header =
        self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header =
        self.extract_base64_authorization_header(authorization_header)
        if base64_authorization_header is None:
            return None

        decoded_base64_authorization_header =
        self.decode_base64_authorization_header(base64_authorization_header)
        if decoded_base64_authorization_header is None:
            return None

        user_credentials =
        self.extract_user_credentials(decoded_base64_authorization_header)
        if user_credentials is None:
            return None

        user = self.user_object_from_credentials(
                        user_credentials[0],
                        user_credentials[1])
        return user
