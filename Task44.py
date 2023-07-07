# Создание исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений в столбце 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()