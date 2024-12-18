def zip_with_function(lst, f):
    return [f(*l) for l in zip(*lst)]
