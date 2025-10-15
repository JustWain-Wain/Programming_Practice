def f(x, symbols):
    """
    Возвращает символы для римских цифр по шаблону.
    """
    l = ("", "0", "00", "000", "01", "1", "10", "100", "1000", "02")
    return ''.join(symbols[int(i)] for i in l[x])

def convert_roman_to_arabic(roman_number):
    """
    Конвертирует римские цифры и числа в арабские. Не реализована проверка правильности ввода римского числа.

    Args:
        roman_number (str): римская цифра или число

    Returns:
        Арабская цифра или число (int)

    Raises:
        TypeError: если в римской цифре содержатся арабские цифры или символы, не являющиеся частью римской системы
        счисления

    Example:
        > convert_roman_to_arabic("IV")
        4
    """
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_numbers = list(map(numbers.get, roman_number))
    for i in range(len(roman_number)-1):
        if arabic_numbers[i] < arabic_numbers[i+1]:
            arabic_numbers[i] = -arabic_numbers[i]
    return sum(arabic_numbers)

def convert_arabic_to_roman(arabic_number):
    """
    Конвертирует арабские цифры в римские.

    Args:
        arabic_number (int): арабская цифра или число

    Returns:
        Римская цифра или число (str)

    Raises:
        TypeError: если параметр не является числом

    Example:
        > convert_arabic_to_roman(8)
        "VIII"
    """
    arabic_number = int(arabic_number)
    thousands = arabic_number // 1000
    arabic_number %= 1000
    hundreds = arabic_number // 100
    arabic_number %= 100
    tens = arabic_number // 10
    arabic_number %= 10
    ones = arabic_number
    return f(thousands, "M") + f(hundreds, "CDM") + f(tens, "XLC") + f(ones, "IVX")

def converter(list_of_nums):
    """
    Позволяет одновременно конвертировать в одном списке арабские в римские числа и наоборот. Проверяет является ли
    элемент римским или арабским числом и вызывает соответствующую функцию, затем воссоздает список конвертированных
    чисел.

    Args:
        list_of_nums (list): список чисел

    Returns:
        Список конвертированных чисел

    Example:
        > converter(["IV", 8, 32, "MMX"])
        [4, 'VIII', 'XXXII', 2010]
    """
    result = []
    for number in list_of_nums:
        is_roman = number[0].isalpha()
        if is_roman:
            result.append(convert_roman_to_arabic(number))
        else:
            result.append(convert_arabic_to_roman(number))
    return result
print("Введите список цифр, разделяя их пробелом (каждое число должно быть в диапазоне от 1 до 3999 включительно): ")
list_of_numbers = input().split()
print("\nРезультат:", converter(list_of_numbers),sep="\n")
input("\nНажмите Enter для выхода.")