def print_results(marks):
    [print(*i) for i in sorted(marks, key=lambda x: x[1])]
