proceeds = float(input("Введите сумму вашей выручки: "))
cost = float(input("Введите сумму ваших затрат: "))
profitability = round((proceeds / cost) * 100)
result = proceeds - cost
profit = proceeds - cost > 0
loss = proceeds - cost < 0
zero = proceeds - cost ==0
if profit:
    print('Ваша компания работает с прибылью ', + result, '. Так держать! '
                                                          'Рентабельность фирмы равна ', + profitability, '%')
    number = int(input("Введите численность сотрудников вашей фирмы: "))
    ppe = result / number
    print('Прибыль на одного сотрудника равна ', ppe)
if zero:
    print('Ваша компания работает с нулевой прибылью!')
if loss:
    print('Ваша компания работает с убытком ', + result, 'или ', + profitability * -1, '%')

