#Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#print(round(number % 1, 2)) --

def find_max_min(my_list):
    maxi = my_list[0]
    mini = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]
        elif my_list[i] < mini:
            mini = my_list[i]
    return[maxi, mini]


def find_diff_max_min(function1):
    return(function1[0] - function1[1])


first_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []
for i in range(len(first_list)):
    if round(first_list[i] % 1, 2) != 0: #операция деление (%) вещественного числа на 1 дает дробную часть
        i = round(first_list[i] % 1, 2)
        new_list.append(i)
function1 = find_max_min(new_list)
function2 = find_diff_max_min(function1)
print(function2)







