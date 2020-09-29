num = int(input("Введите целое положительное число: "))

max = num % 10
while num > 0:
    if max >= num % 10:
        num = num // 10
        print(num)
    else:
        max = num % 10
        print(num)
print('Максимальное число: ', max)