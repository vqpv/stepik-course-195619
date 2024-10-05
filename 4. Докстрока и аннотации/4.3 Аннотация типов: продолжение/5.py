def rotate_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    return chr((ord(letter) + shift - 97) % 26 + 97)

def caesar_cipher(phrase: str, key: int) -> str:
    'Шифр Цезаря'
    result = ""
    for i in phrase:
        if i.isalpha():
            result += rotate_letter(i.lower(), key)
        else:
            result += i
    return result
