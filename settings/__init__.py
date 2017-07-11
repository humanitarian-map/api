import sys


try:
    print("Trying import local settings...", file=sys.stderr)
    from .local import *    # noqa
except ModuleNotFoundError:
    print("Import base settings...", file=sys.stderr)
    from .base import *     # noqa
