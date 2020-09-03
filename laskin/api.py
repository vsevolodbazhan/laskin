from connexion import NoContent


def hello():
    return {"message": "Hello!"}, 200


def extract_numbers(payload):
    a, b = payload["a"], payload["b"]
    return float(a), float(b)


def greater_or_equal(body):
    a, b = extract_numbers(body)

    if a >= b:
        return NoContent, 200
    return NoContent, 204
