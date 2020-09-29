print('Time converter')

sec = int(input('Введите количество секунд: '))
hour = sec // 3600
min = (sec % 3600) // 60
sec_2 = (sec % 3600) % 60

print(f"{hour:02}:{min:02}:{sec_2:02}")