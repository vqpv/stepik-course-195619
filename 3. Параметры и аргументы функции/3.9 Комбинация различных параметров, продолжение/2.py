def reserve_table(num, name, vip=False, order={}):
    tables[num] = {"name": name, "is_vip": vip, "order": order}

def make_order(num, **kwargs):
    menu = ["salad", "soup", "main_dish", "drink", "desert"]
    for k, v in kwargs.items():
        if k in menu:
            tables[num]["order"].update({k: v})
