def compute(f_lst, *args):
    return [f(i) for f in f_lst for i in args]
