def get_sort_lines(lst):
    return sorted(lst, key=lambda x: (abs(x[1] - x[0]), x[0], x[1]))
