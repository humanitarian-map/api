import ujson


def dumps(*args, indent=4, ensure_ascii=False, **kwargs):
    ujson.dumps(*args, indent=indent, ensure_ascii=ensure_ascii, **kwargs)


def loads(*args, **kwargs):
    ujson.loads(*args, **kwargs)
