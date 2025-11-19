"""
Анализ датасета DBpedia (14 категорий).

ЗАДАНИЕ:
Загрузите датасет DBpedia, анализируйте распределение по 14 категориям,
выполните статистический анализ текстов и выявите топ слова по категориям.

ТРЕБОВАНИЯ:
- Загрузить датасет: load_dataset()
- Провести анализ распределения по 14 категориям
- Вычислить статистику заголовков и контента
- Найти топ-25 слов для каждой категории
- Создать bar chart распределения
- Сохранить результаты в dbpedia_results.json
"""

import json
import re
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt


# Настройка стиля графиков
plt.rcParams.update({'font.size': 12})


def load_dbpedia_dataset():
    """Загружает датасет DBpedia из Hugging Face."""
    print("Загрузка датасета DBpedia...")
    dataset = load_dataset("dbpedia_14")
    print("Датасет успешно загружен.")
    return dataset


def preprocess_text(text: str) -> str:
    """Предобрабатывает текст: приведение к нижнему регистру, удаление цифр и пунктуации."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Zа-яА-Я\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_category_name(label: int) -> str:
    """Возвращает название категории по индексу."""
    categories = [
        "Company", "Educational Institution", "Artist", "Athlete",
        "Office Holder", "Mean of Transportation", "Building", "Natural Place",
        "Village", "Animal", "Plant", "Album", "Film", "Written Work"
    ]
    return categories[label]


def analyze_category_distribution(dataset):
    """Анализирует распределение по 14 категориям."""
    labels = [example['label'] for example in dataset['train']]
    label_counts = Counter(labels)
    distribution = {get_category_name(i): label_counts.get(i, 0) for i in range(14)}
    return distribution


def analyze_text_statistics(dataset):
    """Вычисляет статистику для заголовков и контента."""
    title_lengths = []
    content_lengths = []

    for example in dataset['train']:
        title = example['title']
        content = example['content']

        title_lengths.append(len(title.split()))
        content_lengths.append(len(content.split()))

    stats = {
        "title": {
            "mean": float(np.mean(title_lengths)),
            "median": float(np.median(title_lengths)),
            "std": float(np.std(title_lengths)),
            "min": int(np.min(title_lengths)),
            "max": int(np.max(title_lengths))
        },
        "content": {
            "mean": float(np.mean(content_lengths)),
            "median": float(np.median(content_lengths)),
            "std": float(np.std(content_lengths)),
            "min": int(np.min(content_lengths)),
            "max": int(np.max(content_lengths))
        }
    }
    return stats


def extract_top_words_by_category(dataset, top_n: int = 25):
    """Извлекает топ-N слов для каждой категории."""
    category_words = defaultdict(list)

    for example in dataset['train']:
        label = example['label']
        title = example['title']
        content = example['content']

        full_text = title + " " + content
        words = preprocess_text(full_text).split()
        category_words[label].extend(words)

    top_words_by_category = {}
    for label in range(14):
        category_name = get_category_name(label)
        counter = Counter([word for word in category_words[label] if len(word) > 1])
        top_words = [word for word, _ in counter.most_common(top_n)]
        top_words_by_category[category_name] = top_words

    return top_words_by_category


def create_visualization(distribution: Dict[str, int]):
    """Создаёт горизонтальную столбчатую диаграмму распределения по категориям."""
    categories = list(distribution.keys())
    counts = list(distribution.values())

    plt.figure(figsize=(12, 8))
    bars = plt.barh(categories, counts, color='skyblue', edgecolor='navy', alpha=0.8)
    plt.xlabel("Количество примеров")
    plt.title("Распределение по категориям в датасете DBpedia")
    plt.gca().invert_yaxis()  # Самые частые наверху

    # Добавляем числа на конце столбцов
    for i, bar in enumerate(bars):
        plt.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
                 str(counts[i]), va='center', ha='left', fontsize=10, color='gray')

    plt.tight_layout()
    plt.savefig("dbpedia_distribution.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("График сохранён как 'dbpedia_distribution.png'")


def main():
    """Основная функция для выполнения анализа."""
    # Загрузка датасета
    dataset = load_dbpedia_dataset()

    # Анализ распределения по категориям
    print("Анализ распределения по категориям...")
    distribution = analyze_category_distribution(dataset)

    # Статистика текстов
    print("Анализ статистики текстов...")
    text_stats = analyze_text_statistics(dataset)

    # Топ-25 слов по категориям
    print("Извлечение топ-25 слов по категориям...")
    top_words = extract_top_words_by_category(dataset, top_n=25)

    # Визуализация
    print("Создание визуализации...")
    create_visualization(distribution)

    # Сохранение результатов
    results = {
        "category_distribution": distribution,
        "text_statistics": text_stats,
        "top_words_by_category": top_words
    }

    with open("dbpedia_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("Анализ завершён. Результаты сохранены в 'dbpedia_results.json'.")


if __name__ == "__main__":
    main()