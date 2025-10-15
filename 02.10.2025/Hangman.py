def hangman(word):
    """
    Стандартная игра "Виселица", где нужно сначала загадать слово, а затем побуквенно его отгадывать. При неправильной
    попытке теряются очки здоровья, при потере всех очков здоровья полностью игра оканчивается поражением.

    Args:
        word (str): загаданное слово

    Returns:
        Постепенный ход игры
    """
    if any(i.isnumeric() for i in word): return "Введенная строка не является словом."
    health = "♥"*10
    word = word.lower()
    word_length = len(word)
    res = ["_"]*word_length
    word_letters = list(word)
    while res != word_letters and len(health) != 0:
        print("\n" * 10000)
        print(f"Попытки: {health} {len(health)}/10", "\n")
        print(f"Текущий результат: {''.join(res)}", "\n")
        letter = input("Введите букву: ").lower()
        if letter in word:
            for i in range(word_length):
                if letter == word[i]:
                    res[i] = letter
        else:
            health = health[:-1]
    print("")
    return f"Вы отгадали слово \"{word}\"!" if res == word_letters else f"Вы проиграли. Загаданное слово: {word}."

print(hangman(input("Загадайте слово: ")))
input("\nНажмите Enter для выхода.")