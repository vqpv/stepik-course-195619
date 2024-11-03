def filter_collection(f, obj):
    t_obj = type(obj)
    if t_obj == str:
        return "".join(i for i in obj if f(i))
    else:
        return t_obj(i for i in obj if f(i))
