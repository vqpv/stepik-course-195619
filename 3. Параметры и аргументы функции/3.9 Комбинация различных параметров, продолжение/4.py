def reserve_table(num, name, vip=False, order={}):
    tables[num] = {"name": name, "is_vip": vip, "order": order}

def make_order(num, **kwargs):
    menu = ["salad", "soup", "main_dish", "drink", "desert"]
    for k, v in kwargs.items():
        if k in menu:
            tables[num]["order"][k] = tables[num]["order"].get(k, []) + v.split(",")

def delete_order(*, number_table, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]["order"] = {}
    else:
        for k, v in kwargs.items():
            if v:
                tables[number_table]["order"].pop(k, None)
