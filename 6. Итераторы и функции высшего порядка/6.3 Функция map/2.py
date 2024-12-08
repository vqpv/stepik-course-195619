def convert_to(values: list[float|int|str], type_to=int):
    return list(map(type_to, values))
