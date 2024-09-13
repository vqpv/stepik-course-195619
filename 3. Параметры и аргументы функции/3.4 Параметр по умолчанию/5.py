def calculate_per_person(check, count, tips=10):
    return (check  + (check * tips) / 100) / count
