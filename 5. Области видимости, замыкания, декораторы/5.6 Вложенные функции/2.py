def wrap_increment(value):
    def _inc(v):
        return v + 1
    return _inc(value)
