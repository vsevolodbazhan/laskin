from operations import comparison_operation, operator


def hello():
    return {"message": "Hello!"}, 200


def greater_or_equal(body):
    return comparison_operation(data=body, operation=operator.ge)
