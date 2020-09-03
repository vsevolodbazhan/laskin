__all__ = ["operator", "comparison_operation"]

import operator
from decimal import Decimal
from http import HTTPStatus

from connexion import NoContent

FIRST_ARGUMENT_KEYWORD = "a"
SECOND_ARGUMENT_KEYWORD = "b"


def extract_numbers(data):
    a, b = data[FIRST_ARGUMENT_KEYWORD], data[SECOND_ARGUMENT_KEYWORD]
    return Decimal(a), Decimal(b)


def comparison_operation(data, operation):
    a, b = extract_numbers(data=data)

    if operation(a, b) is True:
        return NoContent, HTTPStatus.OK
    return NoContent, HTTPStatus.NO_CONTENT


def mathematical_operation(data, operation):
    a, b = extract_numbers(data=data)

    value = operation(a, b)
    return {"value": f"{value:.2f}"}, HTTPStatus.OK
