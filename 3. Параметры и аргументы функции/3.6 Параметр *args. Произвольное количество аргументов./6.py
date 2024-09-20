def print_goods(*args):
    s = list(filter(lambda x: isinstance(x, str) and x != "", args))
    if s:
        for i, j in enumerate(s):
            print(f'{i + 1}. {j}')
    else:
        print("Нет товаров")
