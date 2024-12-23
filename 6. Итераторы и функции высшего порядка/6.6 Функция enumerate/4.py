def find_different_indexes(s1: str, s2: str) -> list[int]:
    return [i for i, (j1, j2) in enumerate(zip(s1, s2)) if j1 != j2]
