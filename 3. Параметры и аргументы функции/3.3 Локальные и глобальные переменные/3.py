def is_table_free(n):
    return tables[n] is None

def get_free_tables():
    return [i for i in tables if is_table_free(i)]
