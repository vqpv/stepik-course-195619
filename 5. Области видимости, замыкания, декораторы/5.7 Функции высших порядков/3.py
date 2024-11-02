def compute(f_lst, *args):
    result = []
    for i in args:
        for f in f_lst:
            i = f(i)
        result.append(i)
    return result
