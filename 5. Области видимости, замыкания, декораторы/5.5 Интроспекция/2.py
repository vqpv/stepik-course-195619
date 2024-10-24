def check_exist_attrs(obj, lst):
    return {attr: hasattr(obj, attr) for attr in lst}
