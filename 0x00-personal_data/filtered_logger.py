#!/usr/bin/env python3
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """ Redacting sensitive info in logs """
    for field in fields:
        message = re.sub(rf'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = ("[HOLBERTON] %(name)s %(levelname)s "
              "%(asctime)-15s: %(message)s")
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # filter values in record
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
