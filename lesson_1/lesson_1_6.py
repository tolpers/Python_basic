first_dist = int(input("Введите результат пробежки: "))
second_dist = int(input("Какого результата вы хотите добиться? "))
i = 1
print(f"Ваш результат {round(first_dist, 2)} на {i} день")
while first_dist <= second_dist:
    first_dist = first_dist + (first_dist * 0.1)
    i += 1
    print(f"Вы добъетесь результата {round(first_dist, 2)} на {i} день")