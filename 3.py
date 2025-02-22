def check_query(query):
    # Разбиваем запрос на имя и сам запрос
    elements = query.split(', ')
    # Возвращаем только вторую часть, то есть запрос
    return elements[1]

# Список запросов
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Перебираем каждый запрос и выводим результат
for q in queries:
    result = check_query(q)
    print(result)
