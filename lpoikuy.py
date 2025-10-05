import matplotlib.pyplot as plt
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
numb = [8, 3, 9, 17, 66, 43, -100]
numb2 = [20, 0, 56, 32, -78, 57, -30]
plt.figure(figsize=(10, 5))
plt.plot(week, numb, marker='o', linestyle='-', color='green')
plt.plot(week, numb2, marker='o', linestyle='-', color='red')
plt.xlabel('День недели')
plt.ylabel('Температура (°C)')
plt.grid(True)
plt.show()