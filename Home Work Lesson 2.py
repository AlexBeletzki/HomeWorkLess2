# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for num, frut in enumerate(fruits):
    print (str(num) + '.  {:>8}'.format(frut))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

Marvel = ['Captain America', 'Superman', 'Thor', 'Spider-Man', 'Hawkeye', 'Batman', 'Iron Man', 'BlackWidow']
DC = ['Superman', 'Batman', 'WonderWoman', 'Aquaman']

print('Герои Marvel: {}'.format(Marvel))
print('Герои DC: {}'.format(DC))

for mr in Marvel[:]:
    for dc in DC[:]:
        if dc == mr:
            Marvel.remove(dc)
print('The Marvel only Heroes: {}'.format(Marvel))
