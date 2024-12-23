def luhn_algorithm(num):
    result = []
    for i, j in enumerate(list(map(int, str(num)))):
        if i % 2 == 0:
            new_j = j * 2
            if new_j > 9:
                new_j -= 9
            result.append(new_j)
        else:
            result.append(j)
    return sum(result) % 10 == 0
