def is_table_free(n):
    return tables[n] is None

def reserve_table(n, name, is_vip):
    if is_table_free(n):
        tables[n] = {'name': name, 'is_vip': is_vip}

def delete_reservation(n):
    tables[n] = None
