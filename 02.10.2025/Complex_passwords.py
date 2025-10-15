from random import choices, shuffle, randint, choice
from string import ascii_uppercase, ascii_lowercase

def distribution(b_settings, length):
    """
    Случайно и неравномерно распределяет количество символов в каждом виде настроек.

    Args:
        b_settings (list): список булевых значений настроек пароля
        length (int): длина пароля

    Returns:
        Список из количества символов в каждом виде настроек, длина которого зависит от количества выбранных настроек
        пользователем.

    Raises:
        TypeError: если settings не является итерируемым объектом
        ValueError: если length меньше 3

    Example:
        > distribution([0,1,0,1], 10)
        [7,3]
    """
    number_of_conditions = sum(b_settings)
    res = b_settings.copy()
    for i in range(4):
        if res[i] == 1:
            dif = length - sum(res) - number_of_conditions
            res[i] = randint(1, dif)
            number_of_conditions -= 1
    dif = length - sum(res)
    if dif == 0: return res
    res[choice([i for i in range(4) if b_settings[i] == 1])] += dif
    return res


def generate_password(settings="", length=0):
    """
    Генерирует пароль исходя из заданных пользователем условий и длины пароля.

    Args:
        settings (str): набор условий
        length (int): длина пароля

    Returns:
        Пароль (str)

    Example:
        > generate_password("1234", 8)
        ,$tM29Ut
    """
    special = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    nums = "0123456789"
    bool_settings = [0, 0, 0, 0]
    for i in settings:
        match i:
            case "1": bool_settings[0] = 1
            case "2": bool_settings[1] = 1
            case "3": bool_settings[2] = 1
            case "4": bool_settings[3] = 1
    quantity_distribution = distribution(bool_settings, length)
    password = (choices(ascii_lowercase, k = quantity_distribution[0]) +
                choices(ascii_uppercase, k = quantity_distribution[1]) +
                choices(special, k = quantity_distribution[2]) +
                choices(nums, k = quantity_distribution[3]))
    shuffle(password)
    return "".join(password)

print("""Настройки пароля:
1. Наличие нижнего регистра
2. Наличие верхнего регистра
3. Наличие спец. символов
4. Наличие цифр""")
user_settings = input("Выберите настройки пароля (в любом порядке без пробелов): ")
user_password_length = int(input("Введите длину пароля: "))

print("\nРезультат:", generate_password(user_settings, user_password_length), sep="\n")
input("\nНажмите Enter для выхода.")