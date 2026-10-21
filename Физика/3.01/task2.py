import matplotlib.pyplot as plt

# Данные для задания 2 (Y = 10 см)
# Для phi_6 = 7.25 значение X в таблице отсутствует (область кольца)
x = [2.6, 4.15, 5.9, 7.2, 8.6, 21.6, 23.0, 24.5, 26.0]
phi = [2.25, 3.25, 4.25, 5.25, 6.25, 8.25, 9.25, 10.25, 11.25]

plt.figure(figsize=(8, 5))
plt.plot(x, phi, 'ro-', label='Экспериментальные данные')
plt.title(r'Зависимость $\phi(x)$ для поля с кольцом (Y = 10 см)')
plt.xlabel('Координата X, см')
plt.ylabel('Потенциал $\phi$, В')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('graph2.png', dpi=300)
plt.show()