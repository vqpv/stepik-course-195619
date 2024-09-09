def is_table_free(n):
    return tables[n] is None

def reserve_table(n, name):
    if is_table_free(n):
        tables[n] = name

def delete_reservation(n):
    tables[n] = None
