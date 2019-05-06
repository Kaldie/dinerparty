import datetime

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

def load_datetime(value):
  if value is None:
    return None
  print([datetime.datetime.strptime(value,"%Y-%m-%d %H:%M:%S")])
  return datetime.datetime.strptime(value,"%Y-%m-%d %H:%M:%S")
