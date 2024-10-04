def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    '''Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)'''
    new_lst = list(tpl)
    if shift > 0:
        for _ in range(shift):
            new_lst.insert(0, new_lst.pop())
    elif shift < 0:
        for _ in range(abs(shift)):
            new_lst.append(new_lst.pop(0))
    return tuple(new_lst)
