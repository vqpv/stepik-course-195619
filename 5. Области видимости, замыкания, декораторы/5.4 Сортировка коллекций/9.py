def print_order_rating(drivers_rating):
    new_d = {}
    result = {}
    for i in drivers_rating:
        new_d[i[0]] = new_d.get(i[0], []) +[i[1]]
    for k, v in new_d.items():
        result[k] = result.get(k, 0) + sum(v) / len(v)
    [print(*i) for i in sorted(result.items(), key=lambda x: (-x[1], x[0].lower()))]
