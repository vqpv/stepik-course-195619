def red():
    return f'Color is red'

def green():
    return f'Color is green'

def blue():
    return f'Color is blue'

colors = {}
colors[green] = '00FF00'
colors[blue] = '0000FF'
colors[red] = 'FF0000'

for k, v in colors.items():
    print(f'{k()} - {v}')
