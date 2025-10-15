import datetime
from decimal import Decimal

def add(items, title, item_amount, expiration_date=None):
    """
    Добавляет элемент вида {'amount': Decimal(item_amount), 'expiration_date': expiration_date} в значения ключа title
    словаря items.

    Args:
        items (dict): словарь, в который необходимо добавить элемент
        title (str): название продукта, которы необходимо добавить в словарь
        item_amount (Decimal or float or int or str): количество этого продукта
        expiration_date (str): срок годности этого продукта

    Returns:
        None

    Raises:
        AttributeError: если items не является словарем

    Example:
        > add(goods, "вода", Decimal("52"), "2025-10-15")
        > print(goods)
        {'Вода': [{'amount': Decimal('52'), 'expiration_date': datetime.date(2025, 10, 15)}]}
        > print(goods["Вода"])
        [{'amount': Decimal('52'), 'expiration_date': datetime.date(2025, 10, 15)}]
    """
    title = title.capitalize()
    exp_date = None
    if expiration_date is not None:
        expiration_date = expiration_date.split("-")
        exp_date = datetime.date(int(expiration_date[0]), int(expiration_date[1]), int(expiration_date[2]))
    if title not in items.keys():
        items[title] = []
    items[title].append({'amount': Decimal(str(item_amount)), 'expiration_date': exp_date})

def add_by_note(items, note):
    """
    Добавляет элемент вида {'amount': Decimal(item_amount), 'expiration_date': expiration_date} в значения ключа title
    словаря items разделяя note на составляющие title, item_amount, expiration_date.

    Args:
        items (dict): словарь, в который необходимо добавить элемент
        note (str): описание продукта вида "название количество дата"

    Returns:
        None

    Raises:
        AttributeError: если items не является словарем, если note не является строкой

    Example:
        > add_by_note(goods, "пицца 11 2025-11-10")
        > print(goods)
        {'Пицца': [{'amount': Decimal('11'), 'expiration_date': datetime.date(2025, 11, 10)}]}
        > add_by_note(goods, "ягоды 55")
        > print(goods)
        {'Ягоды': [{'amount': Decimal('55'), 'expiration_date': None}]}
    """
    note = note.split()
    title = note[0]
    item_amount = Decimal(note[1])
    if len(note) == 2 or note[-1] == '':
        expiration_date = None
    else:
        expiration_date = note[2]
    add(items, title, item_amount, expiration_date)

def find(items, needle):
    """
    Ищет в словаре items заданное слово или строку и возвращает список продуктов, в названии которых есть это слово или
    эта строка.

    Args:
        items (dict): словарь, в котором необходимо выполнить поиск
        needle (str): строка, которую необходимо найти в названиях продуктов

    Returns:
        list: список названий продуктов, в которых имеется данная строка

    Raises:
        AttributeError: если items не является словарем, если needle не является строкой

    Example:
        > find(goods, "од")
        ["Вода", "Водяная вода"]
    """
    needle = needle.lower()
    result = []
    for title in items.keys():
        if needle in title.lower():
            result.append(title)
    return result

def amount(items, needle):
    """
    Возвращает количество запрошенного продукта needle в items.

    Args:
        items (dict): словарь, в котором необходимо посчитать количество продукта
        needle (str): название продукта

    Returns:
        Decimal: количество продукта needle

    Raises:
        AttributeError: если items не является словарем, если needle не является строкой

    Example:
        > amount(goods, "Вода")
        Decimal("15")
    """
    needle = needle.lower()
    counter = 0
    titles = find(items, needle)
    for title in titles:
        for item in items[title]:
            counter += item['amount']
    return Decimal(counter)

goods = {}

add(goods, "Вода", 3)
add_by_note(goods, "Мясо 10 2025-11-15")
add_by_note(goods, "Вода 7")
add_by_note(goods, "Мясо 2 2025-11-16")
print(find(goods, 'о'))
print(amount(goods, "Мясо"))
print(amount(goods, "Вода"))
print(goods)
