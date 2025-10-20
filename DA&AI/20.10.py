import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# Воссоздаем данные из "Лист2", используя только первую таблицу (до пустых строк)
data = {
    "Инсульт": [1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0],
    "PSV": [np.nan,80,94,80,80,79,74,86,102,74,94,70,73,87,77,82,51,58,80,75,84,75,80,82,81,81,77,82,76,76,50,90,94,78,74],
    "ED": [24.9,13.40,16.90,16.9,19,17,39.6,14,13,27,13,12,10.7,25,11.6,21.4,16,13,12,22,6.2,8,12,18,29.4,10.7,10,21.4,19.6,37,11.6,33.9,23,25,36],
    "TAV": [50.2,32.50,29.60,26.7,45.5,34.7,17.8,28,27,45.6,23.2,32,27,57,34,40.6,43,34.3,42,37,23,26,25,33.9,49,28.6,26,40,41.8,57.2,34.6,51.7,45,43,54],
    "Ri": [0.69,0.77,0.74,0.78,0.8,0.8,0.78,0.76,0.73,0.76,0.74,0.78,0.79,0.84,0.76,0.78,0.77,0.79,0.79,0.73,0.77,0.8,0.77,0.73,0.73,0.76,0.78,0.76,0.76,0.84,0.77,0.73,0.74,0.8,0.77],
    "PI": [1.7,2.20,1.30,1.4,1.5,1.8,1.9,1.2,1.5,1.3,2,2,1.6,2.1,2,1.9,1.2,1.8,2.3,1.4,2.5,1.7,1.6,1.5,1.4,2.3,2.3,1.8,1.5,1.6,2.4,1.4,1.4,1.6,1.3]
}

df = pd.DataFrame(data)

# Удалим строки с пропущенными значениями в 'Инсульт' или других столбцах (кроме PSV, где NaN в первой строке)
df = df.dropna(subset=['Инсульт'])
df['Инсульт'] = df['Инсульт'].astype(int)

# Столбцы для анализа
cols = ['PSV', 'ED', 'TAV', 'Ri', 'PI']

# Функция для вычисления 95% доверительного интервала медианы (метод бутстрэп)
def median_ci_bootstrap(series, n_boot=1000, ci=95):
    if series.dropna().empty:
        return np.nan, np.nan
    boot_medians = []
    series_clean = series.dropna()
    for _ in range(n_boot):
        sample = np.random.choice(series_clean, size=len(series_clean), replace=True)
        boot_medians.append(np.median(sample))
    lower = np.percentile(boot_medians, (100 - ci) / 2)
    upper = np.percentile(boot_medians, 100 - (100 - ci) / 2)
    return lower, upper

# Подготовим данные для графика
plot_data = []

for group in sorted(df['Инсульт'].unique()):
    group_df = df[df['Инсульт'] == group]
    for col in cols:
        med = group_df[col].median()
        lower, upper = median_ci_bootstrap(group_df[col])
        plot_data.append({
            'Группа': f"Группа {group}",
            'Показатель': col,
            'Медиана': med,
            'Нижняя': lower,
            'Верхняя': upper
        })

plot_df = pd.DataFrame(plot_data)

# Построим столбчатую диаграмму с "усами" (доверительный интервал для медианы)
plt.figure(figsize=(12, 12))
bar_positions = np.arange(len(cols))
width = 0.35

for i, group in enumerate(sorted(df['Инсульт'].unique())):
    subset = plot_df[plot_df['Группа'] == f"Группа {group}"]
    offset = (i - 0.5) * width
    plt.bar(bar_positions + offset, subset['Медиана'], width, label=f"Группа {group}", alpha=0.8)
    plt.errorbar(bar_positions + offset, subset['Медиана'],
                 yerr=[subset['Медиана'] - subset['Нижняя'], subset['Верхняя'] - subset['Медиана']],
                 fmt='none', ecolor='black', capsize=5)

plt.xticks(bar_positions, cols)
plt.ylabel('Медиана')
plt.title('Медианы показателей по группам с 95% доверительным интервалом')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.gca()
plt.yaxis.set_major_locator(MultipleLocator(0.5))
plt.show()