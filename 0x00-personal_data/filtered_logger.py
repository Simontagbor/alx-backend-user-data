#!/usr/bin/env python3
"""This module contains the RedactingFormatter class."""
import re
import logging
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Redacts sensitive info in logs."""
    for field in fields:
        message = re.sub(rf'{field}=[^;]*', f'{field}={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """gets a logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler("user_data.log")
    file_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(file_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.
    This class inherits from logging.Formatter
    and redacts sensitive information
    from logs.
    """

    REDACTION: str = "***"
    FORMAT: str = ("[HOLBERTON] %(name)s %(levelname)s "
                   "%(asctime)-15s: %(message)s")
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter class.
        """
        super().__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the record after redacting sensitive information.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
