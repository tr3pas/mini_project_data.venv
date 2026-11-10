import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv('csv/Video_Game_Sales_Final.csv')
sns.set_theme(style="whitegrid")

region_sales = df.groupby('primary_region')['global_sales'].sum().sort_values(ascending=False).reset_index()
print("Сумарні продажі за регіонами:")
print(region_sales)

plt.figure(figsize=(10, 6))
sns.barplot(data=region_sales, x='primary_region', y='global_sales',hue='global_sales', palette='viridis', legend=False)
plt.title("Сумарні продажі за регіонами")
plt.xlabel("Регіон")
plt.ylabel("Продажі (млн копій)")
plt.show()

region_mean_sales = df.groupby('primary_region')['global_sales'].mean().sort_values(ascending=False).reset_index()
print("Серендні продажі за регіонами:")
print(region_mean_sales)


plt.figure(figsize=(10, 6))
sns.barplot(data=region_mean_sales, x='primary_region', y='global_sales',hue='global_sales', palette='viridis', legend=False)
plt.title("Середні продажі за регіонами")
plt.xlabel("Регіон")
plt.ylabel("Продажі (млн копій)")
plt.show()

region_genre_sales = df.groupby(['primary_region', 'genre'])['global_sales'].sum().reset_index()
print("Сумарні продажі за регіонами та жанрами:")
print(region_genre_sales[df['primary_region'] != 'Other'].sort_values(by='global_sales', ascending=False).head(10))

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
