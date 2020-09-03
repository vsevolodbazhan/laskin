__all__ = ["operator", "comparison_operation"]

import operator
from decimal import Decimal
from http import HTTPStatus

from connexion import NoContent

FIRST_ARGUMENT_KEYWORD = "a"
SECOND_ARGUMENT_KEYWORD = "b"


def extract_number(data, keyword):
    number = data[keyword]
    return Decimal(number)


def comparison_operation(data, operation):
    a, b = (
        extract_number(data=data, keyword=FIRST_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=SECOND_ARGUMENT_KEYWORD),
    )

    if operation(a, b) is True:
        return NoContent, HTTPStatus.OK
    return NoContent, HTTPStatus.NO_CONTENT


def mathematical_operation(data, operation):
    a, b = (
        extract_number(data=data, keyword=FIRST_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=SECOND_ARGUMENT_KEYWORD),
    )

    value = operation(a, b)
    return {"value": f"{value:.2f}"}, HTTPStatus.OK
