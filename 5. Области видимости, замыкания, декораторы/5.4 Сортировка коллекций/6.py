def print_goods(lst):
    for i in sorted(lst, key=lambda x: (x['color'].lower(), -x['model'])):
        print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")
