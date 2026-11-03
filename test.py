import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('csv/video_games_sales.csv')
from scipy import stats

""" 1 step """
columns = df.columns.tolist()
for column in columns:
    print(column)
print(df.dtypes)
print(df.head())
print(df.info())
print(df.describe())

df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')

print(df.dtypes)
""" 2 step """
missing_columns = df.isnull().sum()
print("Пропущені значення у стовпцях:")
print(missing_columns)
missing_rows = df.isnull().sum(axis=1)
print("\\nКількість пропущених значень у кожному рядку:")
print(missing_rows[missing_rows > 0])

numerical_columns = ['year', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
for column in numerical_columns:
    if df[column].isnull().sum() > 0:
        mean_value = df[column].mean()
        df[column] = df[column].fillna(mean_value.as_integer_ratio()[0])
        print(f"Заповнено пропущені значення у стовпці '{column}' середнім значенням: {mean_value}")

categorical_columns = ['genre', 'publisher']
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)
        print(f"Заповнено пропущені значення у стовпці '{column}' найчастішим значенням: {mode_value}")

missing_columns = df.isnull().sum()
print("Пропущені значення у стовпцях:")
print(missing_columns)
missing_rows = df.isnull().sum(axis=1)
print("\\nКількість пропущених значень у кожному рядку:")
print(missing_rows[missing_rows > 0])

# """ 3 step """

print(df.dtypes)

# df['year'] = df['year'].astype('Int64')
df['genre'] = df['genre'].astype('category')
df['publisher'] = df['publisher'].astype('category')

print(df.dtypes)
print(df.head())
print(df.info())


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['global_sales'])
plt.title('Box Plot глобальних продажів відеоігор')
plt.xlabel('Глобальні продажі (мільйони одиниць)')
plt.show()




df['Z_Score_Global_Sales'] = stats.zscore(df['global_sales'])

anomalies = df[(df['Z_Score_Global_Sales'] > 3) | (df['Z_Score_Global_Sales'] < -3)]
print("Аномальні записи за Z-Score:")
print(anomalies)

df_cleaned = df[(df['Z_Score_Global_Sales'] <= 3) & (df['Z_Score_Global_Sales'] >= -3)]

df_cleaned = df_cleaned.drop(columns=['Z_Score_Global_Sales'])

print(f"Кількість рядків після видалення аномалій: {df_cleaned.shape[0]}")

df_cleaned.loc[df_cleaned['name'] == 'Super Fun Game', 'global_sales'] /= 2

print(df_cleaned[df_cleaned['name'] == 'Super Fun Game'])

print(df_cleaned.head())

new_anomalies = df_cleaned[(df_cleaned['global_sales'] > 1000) | (df_cleaned['global_sales'] < 0)]
print(f"Кількість аномальних записів після обробки: {new_anomalies.shape[0]}")

df_cleaned.to_csv('csv/Video_Game_Sales_Final.csv', index=False)

print("Очищені дані збережено у файл 'Video_Game_Sales_Final.csv'")