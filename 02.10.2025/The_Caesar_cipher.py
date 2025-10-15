from string import ascii_uppercase, ascii_lowercase

def caesar_encode(string, key=0):
    """
    Автоматически определяет язык сообщения и шифрует его согласно сдвигу по алфавиту.

    Args:
        string (str): исходное сообщение
        key (int): сдвиг, может быть как положительным, так и отрицательным

    Returns:
        Зашифрованное сообщение (str)

    Raises:
        ValueError: если key не является числом

    Example:
        > caesar_encode("Привет мир", 5)
        Фхнжйч снх
    """
    result = ""
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if any(1 for i in ru_alphabet if i in string):
        alphabet_lower = ru_alphabet[:33]
        alphabet_upper = ru_alphabet[33:]
    else:
        alphabet_lower = ascii_lowercase
        alphabet_upper = ascii_uppercase
    len_alphabet = len(alphabet_lower)
    for i in range(len(string)):
        if string[i] in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~ 0123456789":
            result += string[i]
        elif string[i] == string[i].upper():
            result += alphabet_upper[(alphabet_upper.find(string[i]) + key) % len_alphabet]
        else:
            result += alphabet_lower[(alphabet_lower.find(string[i]) + key) % len_alphabet]
    return result

def caesar_decode(string, key=0):
    """
    Автоматически определяет язык сообщения и расшифровывает его согласно сдвигу по алфавиту.

    Args:
        string (str): зашифрованное сообщение
        key (int): сдвиг, может быть как положительным, так и отрицательным

    Returns:
        Расшифрованное сообщение (str)

    Raises:
        ValueError: если key не является числом

    Example:
        > caesar_decode("Фхнжйч снх", 5)
        Привет мир
    """
    result = ""
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if any(1 for i in ru_alphabet if i in string):
        alphabet_lower = ru_alphabet[:33]
        alphabet_upper = ru_alphabet[33:]
    else:
        alphabet_lower = ascii_lowercase
        alphabet_upper = ascii_uppercase
    len_alphabet = len(alphabet_lower)
    for i in range(len(string)):
        if string[i] in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~ 0123456789":
            result += string[i]
        elif string[i] == string[i].upper():
            result += alphabet_upper[(alphabet_upper.find(string[i]) - key) % len_alphabet]
        else:
            result += alphabet_lower[(alphabet_lower.find(string[i]) - key) % len_alphabet]
    return result

print("1. Зашифровать сообщение\n"
      "2. Расшифровать сообщение")
n = input("Выберите действие: ")
user_string = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
if n == "1":
    print("\nРезультат:")
    print(caesar_encode(user_string, offset))
elif n == "2":
    print("\nРезультат:")
    print(caesar_decode(user_string, offset))

input("\nНажмите Enter для выхода.")