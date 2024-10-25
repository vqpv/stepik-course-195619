def create_attrs(obj, lst):
    for attr_name, attr_value in lst:
        setattr(print_goods, attr_name, attr_value)

def check_exist_attrs(obj, lst):
    return {attr: hasattr(obj, attr) for attr in lst}
