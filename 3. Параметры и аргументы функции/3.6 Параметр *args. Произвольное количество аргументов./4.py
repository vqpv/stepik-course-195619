def check_sum(*args):
    print(("verification passed", "not enough")[sum(args) < 50])
