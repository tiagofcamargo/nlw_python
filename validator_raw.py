from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "",
        "elemento3": "123"
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": {"type": "float", "required": True, "empty": False},
            "elemento2": {"type": "string", "required": True, "empty": False},
            "elemento3": {"type": "string", "required": False, "empty": False}
        }
    }
})

response = body_validator.validate(body)

print(response)
print(body_validator.errors)
