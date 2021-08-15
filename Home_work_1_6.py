start = float(input("Введите минимальное количество километров для старта: "))
finish = float(input("Введите максимальное кол-во километров, которое хотите достигнуть: "))
progress = start * 0.1
result = start + progress
final = result - start
days = round(final / progress)
if finish < start:
    print('Вы задали неверное количество километров, которое холтите достигнуть, повторите попытку!')
else:
    while result <= finish:
        result *= 1.1
print('Ответ: на ', + (round((result - start) / progress)), '-й день спортсмен достигнет результата — не менее ',
      + round(finish), 'км.')
