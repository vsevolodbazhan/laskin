__all__ = ["operator", "comparison_operation"]

import operator
from http import HTTPStatus

from connexion import NoContent

FIRST_ARGUMENT_KEYWORD = "a"
SECOND_ARGUMENT_KEYWORD = "b"

TRUE = HTTPStatus.OK
FALSE = HTTPStatus.NO_CONTENT


def extract_numbers(data):
    a, b = data[FIRST_ARGUMENT_KEYWORD], data[SECOND_ARGUMENT_KEYWORD]
    return float(a), float(b)


def comparison_operation(data, operation):
    a, b = extract_numbers(data=data)

    if operation(a, b) is True:
        return NoContent, TRUE
    return NoContent, FALSE
