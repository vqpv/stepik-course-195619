def print_scores(name, *args):
    print("Student name:", name)
    print(*sorted(args), sep="\n")
