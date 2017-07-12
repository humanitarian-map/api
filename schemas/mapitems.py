create = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "project_id": {"type": "string"},
        "description": {"type": "string"},
        "type": {"type": "string"},
        "data": {"type": "object"},
    },
    "required": ["name", "project_id", "type", "data"]
}
