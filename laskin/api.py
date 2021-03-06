import operator

from .operations import comparison_operation, mathematical_operation, range_operation


def less(body):
    return comparison_operation(data=body, operation=operator.lt)


def greater(body):
    return comparison_operation(data=body, operation=operator.gt)


def less_or_equal(body):
    return comparison_operation(data=body, operation=operator.le)


def greater_or_equal(body):
    return comparison_operation(data=body, operation=operator.ge)


def equal(body):
    return comparison_operation(data=body, operation=operator.eq)


def add(body):
    return mathematical_operation(data=body, operation=operator.add)


def substract(body):
    return mathematical_operation(data=body, operation=operator.sub)


def multiply(body):
    return mathematical_operation(data=body, operation=operator.mul)


def divide(body):
    return mathematical_operation(data=body, operation=operator.truediv)


def exponentiate(body):
    return mathematical_operation(data=body, operation=operator.pow)


def within_exclusive_range(body):
    return range_operation(data=body, exclusive=True)


def within_inclusive_range(body):
    return range_operation(data=body, exclusive=False)
