import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv('csv/Video_Game_Sales_Final.csv')

# print(df.info())
# print(df.describe())

# missing = df.isna().sum().sort_values(ascending=False)
# missing_df = pd.DataFrame({
#     "Стовпець": missing.index,
#     "Пропусків": missing.values,
#     "Частка, %": (missing.values / len(df) * 100).round(2),
# })

# plt.figure(figsize=(10, 6))
# ax = sns.barplot(data=missing_df, x="Пропусків", y="Стовпець", palette="viridis")
# plt.title("Кількість пропущених значень за стовпцями")
# plt.tight_layout()
# plt.show()

# # (додатково) карта розташування пропусків
# plt.figure(figsize=(10, 5))
# sns.heatmap(df.isna(), cbar=False, yticklabels=False)
# plt.title("Карта пропущених значень")
# plt.show()

grouped_df = df.groupby(['genre', 'platform']).agg(
    Total_Sales=pd.NamedAgg(column='global_sales', aggfunc='sum'),
    Average_Sales=pd.NamedAgg(column='global_sales', aggfunc='mean')
).reset_index()

print(grouped_df.head(10))

genre_sales = df.groupby('genre')['global_sales'].sum().sort_values(ascending=False).reset_index() # 1 варіант
print("Топ 5 жанрів за сумарними продажами:")
print(genre_sales.head(5))

genre_sales = df.groupby('genre')['global_sales'].sum().nlargest(5).reset_index() # 2 варіант
print("Топ 5 жанрів за сумарними продажами:")
print(genre_sales)

df['region'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

def categorize_region(row):
    if row['na_sales'] > row[['eu_sales', 'jp_sales', 'other_sales']].max():
        return 'na'
    elif row['eu_sales'] > row[['na_sales', 'jp_sales', 'other_sales']].max():
        return 'eu'
    elif row['jp_sales'] > row[['na_sales', 'eu_sales', 'other_sales']].max():
        return 'jp'
    
    else:
        return 'Other'

df['primary_region'] = df.apply(categorize_region, axis=1)

region_sales = df.groupby('primary_region').agg(
    Total_Sales=pd.NamedAgg(column='global_sales', aggfunc='sum')
).reset_index()
print("Загальні продажі за регіонами:")
print(region_sales)

region_sales_sorted = region_sales.sort_values(by='Total_Sales', ascending=False).reset_index(drop=True)
print("Регіони за сумарними продажами (від найбільшого до найменшого):")
print(region_sales_sorted)


top_region = region_sales_sorted.iloc[0]
print(f"Найуспішніший регіон: {top_region['primary_region']} з сумарними продажами {top_region['Total_Sales']} мільйонів одиниць.")

numerical_cols = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
corr_matrix = df[numerical_cols].corr()
print("Кореляційна матриця:")
print(corr_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Кореляційна матриця продажів за регіонами')
plt.show()

genre_platform_region_sales = df.groupby(['genre', 'platform', 'primary_region']).agg(
    Total_Sales=pd.NamedAgg(column='global_sales', aggfunc='sum')
).reset_index()

print("Агреговані продажі за жанрами, платформами та регіонами:")
print(genre_platform_region_sales.head(10))

genre_dummies = pd.get_dummies(df['genre'], prefix='Genre')
platform_dummies = pd.get_dummies(df['platform'], prefix='Platform')
df_encoded = pd.concat([df, genre_dummies, platform_dummies], axis=1)
numeric_columns = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales'] + list(genre_dummies.columns) + list(platform_dummies.columns)
corr_matrix_extended = df_encoded[numeric_columns].corr()
print("Кореляційна матриця з жанрами та платформами:")
print(corr_matrix_extended)

plt.figure(figsize=(20, 15))
sns.heatmap(corr_matrix_extended, annot=False, cmap='coolwarm', linewidths=0.5)
plt.title('Кореляційна матриця між жанрами, платформами та продажами')
plt.show()

df.to_csv('csv/Video_Game_Sales_Final.csv', index=False)