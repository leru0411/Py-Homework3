#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Fn = Fn-1 + Fn-2 
def fibonacci(num):
    numbers_fib = [0]
    first_num = 1
    second_num = 1
    numbers_fib.append(first_num)
    numbers_fib.append( second_num)
    for _ in range(2, num):
        first_num, second_num = second_num, first_num + second_num
        numbers_fib.append(second_num)
    return numbers_fib


def negative_fibonacci(num):
    new_numbers_fib = []
    first_num = 1
    second_num = -1
    new_numbers_fib.append(first_num)
    new_numbers_fib.append(second_num)
    for _ in range(2, num):
        first_num, second_num = second_num, first_num - second_num
        new_numbers_fib.append(second_num)
    new_numbers_fib.reverse()
    return new_numbers_fib


number = 8
print(negative_fibonacci(number) + fibonacci(number))
