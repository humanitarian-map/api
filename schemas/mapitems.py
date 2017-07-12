create = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},
        "data": {"type": "object"}
    },
    "required": ["name", "type", "data"]
}

update = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},
        "data": {"type": "object"}
    },
    "required": ["name", "description", "type", "data"]
}
