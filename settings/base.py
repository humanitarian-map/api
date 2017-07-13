from os import environ as env

DB = {
    "url": {
        "drivername": "postgresql",
        "host": env.get("HUMMAP_DB_HOST", ""),
        "port": env.get("HUMMAP_DB_PORT", "5432"),
        "username": env.get("HUMMAP_DB_USER", ""),
        "password": env.get("HUMMAP_DB_PASSWORD", ""),
        "database": env.get("HUMMAP_DB_NAME", "humanitarianmap")
    },
    "extra_settings": {
        "convert_unicode": True,
        "pool_size": 5
    }
}

ALLOW_ALL_ORIGINS = env.get("HUMMAP_ALLOW_ALL_ORIGINS", "true") in ["true", "True", "TRUE"]
ALLOW_ORIGINS = env.get("HUMMAP_ALLOW_ORIGINS", "http://localhost:3000").split(";")
ALLOW_ALL_HEADERS = env.get("HUMMAP_ALLOW_ALL_HEADERS", "true") in ["true", "True", "TRUE"]
ALLOW_HEADERS_LIST = env.get("HUMMAP_ALLOW_HEADERS_LIST", [])
ALLOW_ALL_METHODS = env.get("HUMMAP_ALLOW_ALL_METHODS", "true") in ["true", "True", "TRUE"]
ALLOW_METHODS_LIST = env.get("HUMMAP_ALLOW_METHODS_LIST", [])
