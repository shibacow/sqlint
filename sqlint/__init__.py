# -*- coding: utf-8 -*-

from sqlint import sqlint

__version__ = '0.1.1'

__all__ = [
    'sqlint'
]


def parse(stmt):
    """

    :param stmt:
    :return:
    """

    return sqlint.parse(stmt)


def check(stmt):
    """

    :param stmt:
    :return:
    """

    return sqlint.check(stmt)
