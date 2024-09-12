def show_list(include_quantities=True):
    for i, j in shopping_list.items():
        if include_quantities:
            print(f'{j}x{i}')
        else:
            print(i)
