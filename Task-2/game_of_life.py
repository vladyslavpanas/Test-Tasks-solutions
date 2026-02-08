import numpy as np
import matplotlib.pyplot as plt
import os

n = 26
# Заповнення випадковими 0 та 1
grid = np.random.randint(0, 2, (n, n))
# Функція, щоб порахувати сусідів для клітинки (x, y)
def get_neighbors(matrix, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Пропускання самої клітинки
            if i == 0 and j == 0:
                continue
            # Перевірка сусідів
            row = (x + i) % n
            col = (y + j) % n
            if matrix[row, col] == 1:
                count += 1
    return count

# Функція для одного кроку гри
def next_generation(current_grid):
    # Створення копії поля для нового стану
    new_grid = np.zeros((n, n))
    for r in range(n):
        for c in range(n):
            neighbors = get_neighbors(current_grid, r, c)
            # Правила гри
            if current_grid[r, c] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_grid[r, c] = 1 # Клітинка живе далі
                else:
                    new_grid[r, c] = 0 # Помирає
            else:
                if neighbors == 3:
                    new_grid[r, c] = 1 # Оживає
    return new_grid
# Зберігання історії кроків
history = []
history.append(grid.copy())
# Виконання 20 ітерацій
temp_grid = grid.copy()
for s in range(20):
    temp_grid = next_generation(temp_grid)
    history.append(temp_grid.copy())
# Малювання початкового стану
plt.imshow(history[0], cmap='Greens')
plt.title("Початок гри")
plt.axis('off')
plt.savefig('game_of_life_start.png', bbox_inches='tight')
plt.close()
# Малювання кінцевого стану (після 20 кроку)
plt.imshow(history[20], cmap='Greens')
plt.title("Стан через 20 кроків")
plt.axis('off')
plt.savefig('game_of_life_end.png', bbox_inches='tight')
plt.close()
print("Головні картинки збережено!")
# Створення папки для всіх кроків
if not os.path.exists('steps'):
    os.mkdir('steps')
# Зберігання кожного кроку як окреме фото
for k in range(len(history)):
    plt.imshow(history[k], cmap='Greens')
    plt.title("Крок номер " + str(k))
    plt.axis('off')
    # Просте ім'я файлу без складного форматування
    plt.savefig("steps/step_" + str(k) + ".png", bbox_inches='tight')
    plt.close()
print("Всі кроки (20 штук) лежать у папці 'steps'")