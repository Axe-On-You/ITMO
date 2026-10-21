import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Настройки графика
fig, ax = plt.subplots(figsize=(8, 7))  # Чуть увеличил высоту для заголовка

# Параметры прямоугольника
x = 5
y = 3
dx = 1.2  # Немного увеличил dx для наглядности
dy = 0.8

# 1. Основной прямоугольник (S = xy)
rect_main = patches.Rectangle((0, 0), x, y, linewidth=2, edgecolor='black', facecolor='#aaddff', label=r'Основное значение $u = xy$')
ax.add_patch(rect_main)

# 2. Приращение по X (y * dx)
rect_dx = patches.Rectangle((x, 0), dx, y, linewidth=2, edgecolor='black', facecolor='#aaffaa', label=r'Вклад $\Delta x$ (линейный)')
ax.add_patch(rect_dx)

# 3. Приращение по Y (x * dy)
rect_dy = patches.Rectangle((0, y), x, dy, linewidth=2, edgecolor='black', facecolor='#aaffaa', label=r'Вклад $\Delta y$ (линейный)')
ax.add_patch(rect_dy)

# 4. Приращение второго порядка (dx * dy)
# Сделал цвет светлее (#ffcccc) для лучшего контраста с черным текстом
rect_dxdy = patches.Rectangle((x, y), dx, dy, linewidth=2, edgecolor='black', facecolor='#ffcccc', label=r'Малость 2-го порядка $\Delta x \Delta y$')
ax.add_patch(rect_dxdy)

# Подписи осей и размеров
plt.text(x/2, -0.4, r'$x$', ha='center', fontsize=14)
plt.text(-0.5, y/2, r'$y$', va='center', ha='right', fontsize=14) # Сдвинул левее

plt.text(x + dx/2, -0.4, r'$\Delta x$', ha='center', fontsize=14)
plt.text(-0.5, y + dy/2, r'$\Delta y$', va='center', ha='right', fontsize=14) # Сдвинул левее

# Подписи площадей внутри
plt.text(x/2, y/2, r'$S = xy$', ha='center', va='center', fontsize=16, fontweight='bold')
plt.text(x + dx/2, y/2, r'$y \cdot \Delta x$', ha='center', va='center', fontsize=12, rotation=90)
plt.text(x/2, y + dy/2, r'$x \cdot \Delta y$', ha='center', va='center', fontsize=12)

# Текст в красном квадрате (delta x delta y)
plt.text(x + dx/2, y + dy/2, r'$\Delta x \Delta y$', ha='center', va='center', fontsize=11, fontweight='bold')

# Настройки осей
ax.set_xlim(-1, x + dx + 1)
ax.set_ylim(-1, y + dy + 1)
ax.set_aspect('equal')
ax.axis('off')  # Скрываем координатные оси

# Легенда
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2)
# Переместил легенду вниз, чтобы не мешала заголовку

# Заголовок в две строки
plt.title(r'Геометрический смысл погрешности произведения:' + '\n' + r'$\Delta u \approx x\Delta y + y\Delta x$', fontsize=16, pad=20)

plt.tight_layout()
plt.savefig('task6_illustration.png', dpi=300)
plt.show()