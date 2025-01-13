def flatten_dict(d):
    result = {}
    for k_1, v_1 in d.items():
        if isinstance(v_1, dict):
            for k_2, v_2 in flatten_dict(v_1).items():
                k = k_1 + "_" + k_2
                result[k] = v_2
        else:
            result[k_1] = v_1
    return result
