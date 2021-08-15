#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = input("Введите целое число: ")

number_2 = number + number
number_3 = number + number + number

print(number, '+', number_2, '+', number_3, '=', int(number) + int(number_2) + int(number_3))

