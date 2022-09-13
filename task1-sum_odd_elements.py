#Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def fill_list(my_list):
    for j in range(5):
        j = int(input('Введите число для заполнения списка: '))
        my_list.append(j)
    return my_list


def sum_odd_elements(my_list):
    sum = 0
    for i in range(1, len(my_list), 2):
        sum += my_list[i]
    print(sum)


the_list = []
fill_list(the_list)
sum_odd_elements(the_list)