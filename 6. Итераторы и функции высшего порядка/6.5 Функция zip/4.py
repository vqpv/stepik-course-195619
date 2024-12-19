def get_info_marks(students, *marks):
    best_marks = [max(*m) for m in zip(*marks)]
    return dict(zip(students, best_marks))
