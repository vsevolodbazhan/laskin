from operations import comparison_operation, operator


def hello():
    return {"message": "Hello!"}, 200


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
