from os import environ as env

DB = {
    "url": {
        "drivername": "postgresql",
        "host": env.get("HUMMAP_DB_HOST", "localhost"),
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

ALLOW_ORIGINS = env.get("HUMMAP_ALLOW_ORIGINS", ["*"])
