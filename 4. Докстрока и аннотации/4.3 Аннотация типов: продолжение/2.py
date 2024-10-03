def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    '''Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'''
    new_lst = lst.copy()
    if shift > 0:
        for _ in range(shift):
            new_lst.insert(0, new_lst.pop())
    elif shift < 0:
        for _ in range(abs(shift)):
            new_lst.append(new_lst.pop(0))
    return new_lst
