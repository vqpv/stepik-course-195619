weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = ((i, weekdays[(i - 3) % 7]) for i in range(1, 365))

for _ in range(77):
    print(next(days))
