#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def find_binary_num(number: int):
    binary_num = ''
    while number > 0:
        binary_num = str(number % 2) + binary_num
        number //= 2
    return binary_num

num = 123
print(find_binary_num(num))
        