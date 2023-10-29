import collections

city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]



num_cities = len(city_list)  # TODO найдите количество городов в списке
res = [sub['population'] for sub in city_list]
total_population = sum([i for i in res])  # TODO найдите общее количество населения
average_population = total_population / num_cities
print(f"Среднее арифметическое населения равно = {total_population}")  # TODO распечатайте среднее арифметическое населения