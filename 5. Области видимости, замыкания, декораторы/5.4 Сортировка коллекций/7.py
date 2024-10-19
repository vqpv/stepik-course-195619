def print_goods(lst):
    new_lst = []
    for l in lst:
        k, v = l.split(": ")
        new_lst.append((k, float(v)))
    [print(f"{i[1]:.2f} - {i[0]}") for i in sorted(new_lst, key=lambda x: (-x[1], x[0].lower()))]
