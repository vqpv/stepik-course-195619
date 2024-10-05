def rotate_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    return chr((ord(letter) + shift - 97) % 26 + 97)
