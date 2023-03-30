many = input('Ввести сумму взноса')
procent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [] # Пустой список
deposit.append(procent.get('ТКБ') * float(many) / 100) # Добавил значение в список.Без float не работало
deposit.append(procent.get('СКБ') * float(many) / 100)
deposit.append(procent.get('ВТБ') * float(many) / 100)
deposit.append(procent.get('СБЕР') * float(many) / 100)
print("Максимальная сумма заработка= ", (round(max(deposit), 3))) # Находит максимальное значение в списке

