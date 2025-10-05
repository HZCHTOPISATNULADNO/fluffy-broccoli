import matplotlib.pyplot as plt

labels = ['Технологии', 'Финансы', 'Здравоохранение', 'Потребительские товары']
sizes = [4, 32, 56, 8]
explode = (0.1, 0, 0, 0)  # "взорвать" первый кусок

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Состав портфеля акций')
plt.axis('equal')  # Равные оси обеспечивают, что диаграмма будет круглой.
plt.show()