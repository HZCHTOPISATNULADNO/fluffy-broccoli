import matplotlib.pyplot as plt
fruits = ['персик', 'драконий фрукт', 'яблоко']
numb = [975, 243, 1057]
plt.figure(figsize = (12, 8))
plt.bar(fruits, numb, color = ['black', 'red', 'green'])
plt.xlabel('Фрукты')
plt.ylabel('На складе:')
plt.grid(True)
plt.show()