income = int(input('Введите доход предприятия: '))
loss = int(input('Введите убытки предприятия: '))
if income < loss:
    print('Ваша компания приносит убытки')
else:
    pers = int(input('Введите количество работников на предприятии: '))
    money = income / loss
    pers_money = income / pers
    print(f'Рентабельность прибыли составляет: {round(money, 2)}')
    print(f'Прибыль на одного сотрудника составляет: {round(pers_money, 2)}')
