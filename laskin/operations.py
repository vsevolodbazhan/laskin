__all__ = ["operator", "comparison_operation"]

import operator
from decimal import Decimal
from http import HTTPStatus

from connexion import NoContent

FIRST_ARGUMENT_KEYWORD = "a"
SECOND_ARGUMENT_KEYWORD = "b"
THIRD_ARGUMENT_KEYWORD = "c"

TRUE_CODE = HTTPStatus.OK
FALSE_CODE = HTTPStatus.NO_CONTENT


def extract_number(data, keyword):
    number = data[keyword]
    return Decimal(number)


def comparison_operation(data, operation):
    a, b = (
        extract_number(data=data, keyword=FIRST_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=SECOND_ARGUMENT_KEYWORD),
    )

    if operation(a, b) is True:
        return NoContent, TRUE_CODE
    return NoContent, FALSE_CODE


def mathematical_operation(data, operation):
    a, b = (
        extract_number(data=data, keyword=FIRST_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=SECOND_ARGUMENT_KEYWORD),
    )

    value = operation(a, b)
    return {"value": f"{value:.2f}"}, HTTPStatus.OK


def range_operation(data, exclusive=True):
    a, b, c = (
        extract_number(data=data, keyword=FIRST_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=SECOND_ARGUMENT_KEYWORD),
        extract_number(data=data, keyword=THIRD_ARGUMENT_KEYWORD),
    )

    if a > b and a < c:
        return NoContent, TRUE_CODE

    if exclusive is False:
        if a == b or a == c:
            return NoContent, TRUE_CODE

    return NoContent, FALSE_CODE
