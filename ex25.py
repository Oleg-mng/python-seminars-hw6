# Задача 7
# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input ('Введите число N: '))
# pr = 1
# for i in range(1, n+1):
#     pr = pr*i
#     print (pr, end= ', ')
# pr = 1

n = int(input('Введите число N: '))
# q=lambda pr, i: pr*i
# q = map(lambda pr : pr*i range(1, n+1))
q=lambda pr: [i*pr for i in range(1, n+1)]
print(q(1))

# print(tuple(filter(lambda num: my_list.count(num) == 1, my_list)))
