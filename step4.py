import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style='whitegrid')


df = pd.read_csv('csv/Video_Game_Sales_Final.csv')

annual = df.groupby('year')['global_sales'].sum()

trend_all = np.poly1d(np.polyfit(annual.index,annual.values, 1))
future = np.arange(2021, 2026)

# print(trend_all(future).round())

# plt.figure(figsize=(12,8))
# plt.plot(annual.index, annual.index, marker='o', color='red', label='Реальні продажі')
# all_years = np.arange(annual.index.min(), 2026)
# plt.plot(all_years, trend_all(all_years), color='b', marker='o', label='Тренд')
# plt.scatter(future, trend_all(future), color='black', zorder=3, label='Прогноз 2021-2026')
# plt.legend()
# plt.show()

# clean = annual[annual.index <= 2015]
# recent = annual[annual.index >= 2008]

# trend_recent = np.poly1d(np.polyfit(recent.index, recent.values, 1))
# future = np.arange(2016, 2021)

# print(trend_recent(future).round())


# plt.figure(figsize=(12,8))
# plt.plot(clean.index, clean.values, marker='o', color='red', label='Реальні продажі')
# plt.plot(recent.index, recent.values, marker='o', color='blue', label='Тренд з 2008 до 2015')
# plt.plot(future, trend_recent(future), color='black', marker='o', label='Прогноз')
# plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
# plt.xlabel('Рік')
# plt.ylabel('Продажі (мільйони одиниць)')
# plt.legend()
# plt.show()

# sns.set_theme(style="whitegrid")

# df = pd.read_csv("csv/Video_Game_Sales_Final.csv")
# print(df.shape)
# print(df.head())

# top_genres = df.groupby('genre')['global_sales'].sum().sort_values(ascending=False).head(5)
# top_platforms = df.groupby('platform')['global_sales'].sum().sort_values(ascending=False).head(5)
# median_genres = df.groupby('genre')['global_sales'].median().sort_values(ascending=False).head(5)
# print(top_genres.round())
# print(top_platforms.round())
# print(median_genres.round(2))

# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# axes[0].barh(top_genres.index, top_genres.values, color='steelblue')
# axes[0].invert_yaxis()
# axes[0].set_title('Топ-5 жанрів за весь час')
# axes[0].set_xlabel('Продажі, млн копій')
# axes[1].barh(top_platforms.index, top_platforms.values, color='darkorange')
# axes[1].invert_yaxis()
# axes[1].set_title('Топ-5 платформ за весь час')
# axes[1].set_xlabel('Продажі, млн копій')
# plt.tight_layout()
# plt.show()

# sns.set_theme(style="whitegrid")

# df = pd.read_csv("csv/Video_Game_Sales_Final.csv")

# recent_games = df[(df['year'] >= 2013) & (df['year'] <= 2015)]
# recent_platforms = recent_games.groupby('platform')['global_sales'].sum().sort_values(ascending=False).head(6)
# recent_genres = recent_games.groupby('genre')['global_sales'].sum().sort_values(ascending=False).head(5)
# print(recent_platforms.round())
# print(recent_genres.round())
# print('PS2 2013-2015:', recent_games[recent_games['platform'] == 'PS2']['global_sales'].sum())

# fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# axes[0].barh(recent_platforms.index, recent_platforms.values, color='seagreen')
# axes[0].invert_yaxis()
# axes[0].set_title('Платформи 2013–2015')
# axes[0].set_xlabel('Продажі, млн копій')
# axes[1].barh(recent_genres.index, recent_genres.values, color='purple')
# axes[1].invert_yaxis()
# axes[1].set_title('Жанри 2013–2015')
# axes[1].set_xlabel('Продажі, млн копій')
# plt.tight_layout()
# plt.show()


"""

як розробникам оптимізувати продажі?

"""
df = df[df['year'] >= 2010]

df['year'] = pd.to_numeric(df['year'], errors='coerce') 
df = df[df['year'].between(1980, 2020)].copy()
df['year'] = df['year'].astype(int)

sns.color_palette('colorblind', as_cmap=True)

region_sales = df.groupby(['primary_region','year'])['global_sales'].sum().sort_values(ascending=False).reset_index()
print("Сумарні продажі за регіонами:")
print(region_sales.head(10))

plt.figure(figsize=(12, 8))
sns.barplot(data=region_sales, x='year', y='global_sales', hue='primary_region')
plt.title("Сумарні продажі за регіонами")
plt.xlabel("Рік")
plt.ylabel("Продажі (млн копій)")
plt.show()


genre_sales = df.groupby(['genre', 'year'])['global_sales'].sum().sort_values(ascending=False).reset_index()
print("Сумарні продажі за жанрами:")
print(genre_sales.head(10))

plt.figure(figsize=(12, 8))
sns.barplot(data=genre_sales, x='year', y='global_sales', hue='genre',)
plt.title("Сумарні продажі за жанрами")
plt.xlabel("Рік")
plt.ylabel("Продажі (млн копій)")
plt.show()

platform_sales = df.groupby(['platform', 'year'])['global_sales'].sum().sort_values(ascending=False).reset_index()
print("Сумарні продажі за платформами:")
print(platform_sales.head(10))

plt.figure(figsize=(12, 8))
sns.barplot(data=platform_sales, x='year', y='global_sales', hue='platform')
plt.title("Сумарні продажі за платформами")
plt.xlabel("Рік")
plt.ylabel("Продажі (млн копій)")
plt.show()

region_genre_sales = df.groupby(['primary_region', 'genre'])['global_sales'].sum().reset_index()
print("Сумарні продажі за регіонами та жанрами:")
sorted_region_genre_sales = region_genre_sales[df['primary_region'] != 'Other'].sort_values(by='global_sales', ascending=False).head(10)
print(sorted_region_genre_sales)

plt.figure(figsize=(12, 8))
sns.barplot(data=sorted_region_genre_sales, x='primary_region', y='global_sales', hue='genre')
plt.title("Сумарні продажі за регіонами та жанрами")
plt.xlabel("Регіон")
plt.ylabel("Продажі (млн копій)")
plt.show()

genre_dummies = pd.get_dummies(region_genre_sales['genre'], prefix='Genre')
primary_region_dummies = pd.get_dummies(region_genre_sales['primary_region'], prefix='Primary_Region')
df_encoded = pd.concat([region_genre_sales, genre_dummies, primary_region_dummies], axis=1)
numeric_columns = ['global_sales'] + list(genre_dummies.columns) + list(primary_region_dummies.columns)
corr_matrix_extended = df_encoded[numeric_columns].corr()
print("Кореляційна матриця з жанрами та регіонами:")
print(corr_matrix_extended)

plt.figure(figsize=(20, 15))
sns.heatmap(corr_matrix_extended, annot=False, cmap='coolwarm', linewidths=0.5)
plt.title('Кореляційна матриця між жанрами, регіонами та продажами')
plt.show()
