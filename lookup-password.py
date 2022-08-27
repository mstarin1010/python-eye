from gi.repository import Secret

def on_password_lookup(source, result, unused):
    password = Secret.password_lookup_finish(result)
    # password will be null, if no matching password found

Secret.password_lookup(EXAMPLE_SCHEMA, { "number": "8", "even": "true" },
                       None, on_password_lookup)
