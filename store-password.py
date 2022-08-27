from gi.repository import Secret

def on_password_stored(source, result, unused):
    Secret.password_store_finish(result)
    # ... do something now that the password has been stored

# The attributes used to later lookup the password. These
# attributes should conform to the schema.
attributes = {
    "number": "8",
    "string": "eight",
    "even": "true"
}

Secret.password_store(EXAMPLE_SCHEMA, attributes, Secret.COLLECTION_DEFAULT,
                      "The label", "the password", None, on_password_stored)
