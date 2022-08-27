from gi.repository import Secret

EXAMPLE_SCHEMA = Secret.Schema.new("org.mock.type.Store",
    Secret.SchemaFlags.NONE,
    {
        "number": Secret.SchemaAttributeType.INTEGER,
        "string": Secret.SchemaAttributeType.STRING,
        "even": Secret.SchemaAttributeType.BOOLEAN,
    }
)
