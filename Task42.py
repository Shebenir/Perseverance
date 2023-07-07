# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
# Найти минимальное значение population
min_population = data['population'].min()

# Отфильтровать данные с минимальным значением population
min_population_data = data[data['population'] == min_population]

# Найти максимальное значение households в отфильтрованных данных
max_households = min_population_data['households'].max()

# Вывести результат
print("Максимальное количество домохозяйств в зоне с минимальным значением population:", max_households)