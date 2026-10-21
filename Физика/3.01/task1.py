import matplotlib.pyplot as plt

# Данные для задания 1 (Y = 10 см)
x = [2.95, 7.25, 12.0, 16.3, 21.2, 25.5]
phi = [1.85, 3.85, 5.85, 7.85, 9.85, 11.85]

plt.figure(figsize=(8, 5))
plt.plot(x, phi, 'bo-', label='Экспериментальные данные')
plt.title(r'Зависимость $\phi(x)$ для плоского конденсатора (Y = 10 см)')
plt.xlabel('Координата X, см')
plt.ylabel('Потенциал $\phi$, В')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('graph1.png', dpi=300)
plt.show()