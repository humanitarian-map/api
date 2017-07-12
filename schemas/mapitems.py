create = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},
        "data": {"type": "object"},
    },
    "required": ["name", "type", "data"]
}
