from humps import camelize

def _post_attributes(value, camel_case=True):
    return {
        "data": {
            "attributes": camelize(value) if camel_case else value
        }
    }
