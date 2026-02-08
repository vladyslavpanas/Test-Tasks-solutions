import random
import matplotlib.pyplot as plt

# Функція для пошуку найбільшої глибини
def find_max_depth(heights):
    n = len(heights)
    max_d = 0
    # Прохід по кожному елементу (крім крайніх)
    for i in range(n):
        # Знаходження найвищої точки зліва
        left_max = max(heights[:i]) if i > 0 else 0
        # Знаходження найвищої точки справа
        right_max = max(heights[i+1:]) if i < n-1 else 0
        water_level = min(left_max, right_max)
        depth = water_level - heights[i]
        if depth > max_d:
            max_d = depth    
    return max_d

# Функція для створення та збереження графіка
def save_lake_plot(data, depth, title, filename, line_color='blue'):
    plt.figure(figsize=(10, 5))
    plt.plot(data, 'o-', color=line_color)
    plt.title(title + " | Depth: " + str(depth))
    plt.xlabel("Index")
    plt.ylabel("Height")
    plt.grid(True)
    
    # Зберігаємо фото, як і було в оригіналі
    plt.savefig(filename)
    print("File saved as:", filename)
    plt.close()

# Готові дані
sample_data = [2, 7, 25, 14, 14, 21, 20, 6, 13, 3, 23, 14, 1, 8, 1, 8, 16, 21, 2, 17, 7, 5, 20, 17, 18, 10]
sample_res = find_max_depth(sample_data)
print("Sample data:", sample_data)
print("Maximum depth (sample):", sample_res)
save_lake_plot(sample_data, sample_res, "Sample data", "sample_data.png")

# Рандомні дані
random_data = []
for _ in range(26):
    random_data.append(random.randint(0, 26))
random_res = find_max_depth(random_data)
print("\nRandom data:", random_data)
print("Maximum depth (random):", random_res)
save_lake_plot(random_data, random_res, "Random data", "random_data.png", line_color='orange')