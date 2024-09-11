shopping_list = {}


def add_item(name, count=1):
    shopping_list[name] = shopping_list.get(name, 0) + count
