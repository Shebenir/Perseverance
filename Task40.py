# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
# Загрузка данных из файла CSV
data = pd.read_csv('sample_data/california_housing_train.csv')

# Фильтрация данных по количеству жителей от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости домов
average_price = filtered_data['median_house_value'].mean()

# Вывод результата
print("Средняя стоимость дома с количеством жителей от 0 до 500: ", average_price )