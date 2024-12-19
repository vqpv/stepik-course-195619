def get_info_marks(students, *marks):
    d = {}
    best_marks = [max(*m) for m in zip(*marks)]
    worst_marks = [min(*m) for m in zip(*marks)]
    for i, j in enumerate(students):
        d[j] = d.get(j, {"best": best_marks[i], "worst": worst_marks[i]})
    return d
