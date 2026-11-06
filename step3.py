import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid")

df = pd.read_csv('csv/Video_Game_Sales_Final.csv')
print(df.shape)
print(df.head())
print(df.info())

annual = df.groupby('year')['global_sales'].sum()
print(annual.tail(8))

annual = annual[annual.index <= 2015]

print(annual.tail(8))

# plt.figure(figsize=(12, 6))
# plt.plot(annual.index, annual.values, marker='o', color='b', label='Сумарні глобальні продажі')
# plt.title('Сумарні глобальні продажі відеоігор за роками')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.lineplot(x=annual.index, y=annual.values, marker='o', color='b', label='Сумарні глобальні продажі')
# plt.title('Сумарні глобальні продажі відеоігор за роками')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()


# x = annual.index.values
# y = annual.values

# coefficients = np.polyfit(x, y, 1)
# print(f"Коефіцієнти лінійної регресії: {coefficients}")

# trend_line = np.poly1d(coefficients)
# print(f"Трендова лінія: {trend_line}")
# print(f"Трендова лінія: {trend_line(2010)}")

# plt.figure(figsize=(12, 6))
# plt.plot(x, y, marker='o', color='b', label='Сумарні глобальні продажі')
# plt.plot(x, trend_line(x), color='r', linestyle='--', label='Трендова лінія')
# plt.title('Сумарні глобальні продажі відеоігор за роками з трендовою лінією')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()

# trend_line2 = np.poly1d(np.polyfit(x, y, 2))
# trend_line3 = np.poly1d(np.polyfit(x, y, 3))

# plt.figure(figsize=(12, 6))
# plt.plot(x,y, marker='o', color='b', label='Сумарні глобальні продажі')
# plt.plot(x, trend_line(x), color='r', linestyle='--', label='Трендова лінія')
# plt.plot(x, trend_line2(x), color='g', linestyle='--', label='Квадратична трендова лінія')
# plt.plot(x, trend_line3(x), color='purple', linestyle='--', label='Кубічна трендова лінія')
# plt.legend()
# plt.show()


# top_genre = (df.groupby('genre')
#              ['global_sales'].sum()
#              .sort_values(ascending=False)
#              .head(10)
#              .reset_index())

# plt.figure(figsize=(12,7))
# sns.barplot(data=top_genre, x='global_sales', y='genre', hue='genre', palette='viridis', legend=False)
# plt.title('Топ 10 жанрів за продажами')
# plt.xlabel('Продажі')
# plt.ylabel('Жанр')
# plt.show()

# color = sns.color_palette("Set2", len(top_genre))

# plt.figure(figsize=(12,7))
# plt.bar(top_genre['genre'], top_genre['global_sales'],color=color)
# plt.gca().invert_yaxis()
# plt.title('Топ 10 жанрів за продажами')
# plt.xlabel('Продажі')
# plt.ylabel('Жанр')
# plt.show()



# platform_sales = (df.groupby('platform')['global_sales'].sum().reset_index())



# plt.figure(figsize=(12, 8))
# sns.boxplot(data=df, x='platform', y='global_sales',
#             hue='platform', palette='Set2', legend=False)
# plt.xticks(rotation=45)
# plt.show()

# plt.figure(figsize=(12, 8))
# sns.boxplot(x='primary_region', y='global_sales', data=df, palette='Set1', hue='primary_region', legend=False)
# plt.title('Розподіл продажів за регіонами')
# plt.xlabel('Регіон')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.show()

print(df[['genre', 'platform', 'primary_region', 'global_sales']].isnull().sum())

df = df.dropna(subset=['genre', 'platform', 'primary_region'])

numerical_cols = ['global_sales', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales']

corr_matrix = df[numerical_cols].corr()

print("Кореляційна матриця:")
print(corr_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Кореляційна матриця продажів за регіонами')
plt.show()