def reserve_table(num, name, vip=False):
    tables[num] = {"name": name, "is_vip": vip}
