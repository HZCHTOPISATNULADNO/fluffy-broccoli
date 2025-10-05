import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
df = pd.read_csv('https://raw.githubusercontent.com/Grossmend/CSV/master/titanic/data.csv')
print(df.head())
df1 = df[["Age"]]
print(df1)
age = [i for i in df1['Age'] if str(i) != 'nan']
print(sum(age)/len(age))
survived_ages = df[df['Survived'] == 1]['Age']
not_survived_ages = df[df['Survived'] == 0]['Age']
print(survived_ages.head())
print(not_survived_ages.head())
mu_survived = survived_ages.mean()
print(mu_survived)
mu_not_survived = not_survived_ages.mean()
print(mu_not_survived)
plt.figure(figsize=(12, 7))
sigma_survived = survived_ages.std()
sigma_not_survived = not_survived_ages.std()
sns.kdeplot(survived_ages, label=f'Выжившие (μ={mu_survived:.1f}, σ={sigma_survived:.1f})', color='dodgerblue', fill=True, alpha=0.2)
plt.legend(fontsize=11)
sns.kdeplot(not_survived_ages, label=f'Погибшие (μ={mu_not_survived:.1f}, σ={sigma_not_survived:.1f})', color='darkorange', fill=True, alpha=0.2)
plt.title('Гауссовское распределение возрастов на Титанике', fontsize=16)
plt.xlabel('Возраст', fontsize=12)
plt.ylabel('Плотность вероятности', fontsize=12)
age_new_passenger = 24
prob_density_survived = norm.pdf(age_new_passenger, loc=mu_survived, scale=sigma_survived)
prob_density_not_survived = norm.pdf(age_new_passenger, loc=mu_not_survived, scale=sigma_not_survived)
plt.axvline(x=age_new_passenger, color='red', linestyle='--', label=f'Пассажир, 30 лет')
plt.text(age_new_passenger + 2, prob_density_survived, f'{prob_density_survived:.4f}', color='dodgerblue')
plt.text(age_new_passenger + 2, prob_density_not_survived, f'{prob_density_not_survived:.4f}', color='darkorange')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
