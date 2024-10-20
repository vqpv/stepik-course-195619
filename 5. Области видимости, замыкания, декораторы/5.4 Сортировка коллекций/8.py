def print_best_and_worst_laureate(d):
    new_d = {}
    for k, i in d.items():
        new_d[i] = new_d.get(i, 0) + 1
    sorted_new_d = sorted(new_d.items(), key=lambda x: x[1])
    print(*sorted_new_d[-1], sep=", ")
    print(*sorted_new_d[0], sep=", ")
