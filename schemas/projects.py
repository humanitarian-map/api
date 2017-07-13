update = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "slug": {"type": "string"},
        "description": {"type": "string"},
        "start_date": {"type": "string"},
        "end_date": {"type": "string"},
        "zoom": {"type": "integer"},
        "center_point": {
            "type": "array",
            "items": {"type": "number"}
        }
    },
    "required": ["name", "slug", "description", "start_date", "end_date", "zoom", "center_point"]
}
