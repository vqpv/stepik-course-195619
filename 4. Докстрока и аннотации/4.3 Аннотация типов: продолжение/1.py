from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    "Находит первый дубль в списке"
    dubles = {}
    for w in [i.lower() for i in words]:
        if words.count(w) > 1 and w not in dubles:
            dubles.update({w: words[words.index(w) + 1:].index(w)})
    if dubles:
            return min(dubles, key=dubles.get)
