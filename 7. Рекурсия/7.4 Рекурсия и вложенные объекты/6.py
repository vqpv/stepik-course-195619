def find_level_element(n, lst, lvl=1):
    if isinstance(lst, list):
        for i in lst:
            if n == i:
                return lvl
            elif isinstance(i, list):
                result = find_level_element(n, i, lvl + 1)
                if result != -1:
                    return result
    return -1
