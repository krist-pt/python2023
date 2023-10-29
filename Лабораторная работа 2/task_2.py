city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

res = [sub['population'] for sub in city_list]
max_population = 5  # Пороговое значение для населения
num_cities = len([i for i in res if i<=max_population]) # TODO найдите количество городов с населением меньшн 5 млн.

print(f"Количество городов с население до 5 млн. жителей равно = {num_cities}")
