def check_winners(list_of_competitors, score=0):
    """
    Проверяет попал ли score в тройку наибольших значений в list_of_competitors.

    Args:
        list_of_competitors (list): список, который содержит количество баллов каждого участника олимпиады
        score (int): количество баллов конкретного участника.

    Returns:
        "Вы в тройке победителей!": если score входит в тройку наибольших значений в list_of_competitors
        "Вы не попали в тройку победителей.": если score не входит в тройку наибольших значений в list_of_competitors

    Raises:
        ValueError: Если score не является числом, если list_of_competitors содержит значения, не являющиеся числами

    Example:
        > check_winners([20, 48, 52, 1, 15], 52)
        "Вы в тройке победителей!"
    """
    unique_scores = list(set(list_of_competitors))  # Преобразуем list_of_competitors в список из уникальных баллов
    unique_scores.sort(reverse=True)
    return "\nВы в тройке победителей!" if score in unique_scores[:3] else "\nВы не попали в тройку победителей."

student_score = int(input("Введите количество баллов: "))
competitors = map(int, input("Введите список баллов (оставьте пустым для использования данного в задаче значения): \n").split())
if not competitors:     # Если пользователь не ввёл значения, то списком баллов становится данный в задаче список
    competitors = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
    print(competitors)
print(check_winners(competitors, student_score))
input("\nНажмите Enter для выхода.")