import datetime
import decimal
import uuid
import json


class JSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time/timedelta,
    decimal types, and generators.
    """
    def default(self, o):
        # For Date Time string spec, see ECMA 262
        # http://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith("+00:00"):
                r = r[:-6] + "Z"
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, datetime.timedelta):
            return str(o.total_seconds())
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, uuid.UUID):
            return str(o)
        elif hasattr(o, "as_dict"):
            return o.as_dict()
        elif hasattr(o, "__getitem__"):
            try:
                return dict(o)
            except:
                pass
        elif hasattr(o, "__iter__"):
            return [i for i in o]
        return super(JSONEncoder, self).default(o)


def dumps(*args, indent=4, ensure_ascii=False, cls=JSONEncoder, **kwargs):
    return json.dumps(*args, indent=indent, ensure_ascii=ensure_ascii, cls=cls, **kwargs)


def loads(*args, **kwargs):
    return json.loads(*args, **kwargs)
