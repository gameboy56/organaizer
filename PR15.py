# ------------------------- TASK 1 -------------------------


# ЗАДАЧА 1: Игра "Лабиринт"
# primer: з10001лфммн100110011010л1


labyrinth_string = input("Введите строку из 25 символов, представляющую лабиринт: ")

# проверка того что введено 25 символов
if len(labyrinth_string) != 25:
   print("Ошибка: нужно ввести ровно 25 символов!")
else:
   # ==================== ЗАДАНИЕ 1.1 ====================

   # лабиринт в виде 5 строк по 5 символов
   print("\n=== Задание 1.1: Лабиринт ===\n")
   print("Лабиринт:")
   for i in range(5):
       start_index = i * 5
       end_index = start_index + 5
       print(labyrinth_string[start_index:end_index])

   # ==================== ЗАДАНИЕ 1.2 ====================

   # координаты входа "н"
   print("\n=== Задание 1.2: Координаты входа ===\n")
   entrance_index = labyrinth_string.find("н")

   # что если вход найден
   if entrance_index != -1:
       entrance_row = entrance_index // 5
       entrance_col = entrance_index % 5
       print(f"Вход находится в строке {entrance_row}, столбце {entrance_col}")
   else:
       print("Вход 'н' не найден в лабиринте!")
       entrance_row = -1
       entrance_col = -1

   # ==================== ЗАДАНИЕ 1.3 ====================

   # координаты выхода "ф"
   print("\n=== Задание 1.3: Координаты выхода ===")
   exit_index = labyrinth_string.find("ф")

   # это если выход найден
   if exit_index != -1:
       exit_row = exit_index // 5
       exit_col = exit_index % 5
       print(f"Выход находится в строке {exit_row}, столбце {exit_col}")
   else:
       print("Выход 'ф' не найден в лабиринте!")
       exit_row = -1
       exit_col = -1

   # ==================== ЗАДАНИЕ 1.4 ====================

   print("\n=== Задание 1.4: Расстояние между входом и выходом ===")
   if entrance_index != -1 and exit_index != -1:
       # манхэтанское расстояние
       distance = abs(entrance_row - exit_row) + abs(entrance_col - exit_col)
       print(f"Манхэттенское расстояние между входом и выходом: {distance} шагов")
   else:
       print("Не удалось вычислить расстояние (вход или выход не найден)")

   # ==================== ЗАДАНИЕ 1.5 ====================

   # осуществляется подсчет монет
   print("\n=== Задание 1.5: Подсчет монет ===")
   coins_count = labyrinth_string.count("м")

   # вывод: монеты в формате Монета x2 или Монета Монета
   if coins_count > 0:
       coins_display = "🟡" * coins_count
       print(f"Количество монет в лабиринте: {coins_count}")
       print(f"Монеты: {coins_display}")
   else:
       print("Монет в лабиринте нет")

   # ==================== ЗАДАНИЕ 1.6 ====================
   # подсчет здоровья
   print("\n=== Задание 1.6: Здоровье игрока ===")
   start_hp = 100

   # подсчет ловушек и врагов
   traps_count = labyrinth_string.count("л")
   enemies_count = labyrinth_string.count("з")

   # вычисление урона
   trap_damage = traps_count * 10
   enemy_damage = enemies_count * 50
   total_damage = trap_damage + enemy_damage

   # вычисление: оставшееся здоровье
   remaining_hp = start_hp - total_damage

   # ограничиваем чтобы здоровье не было отрицательным
   if remaining_hp < 0:
       remaining_hp = 0

   # вычисление количества сердечек
   # каждое полное сердце = 10 хп оставшегося здоровья
   # каждое пустое сердце = 10 хп потерянного здоровья
   hearts_count = remaining_hp // 10
   lost_hearts_count = total_damage // 10

   # ограничиваем максимальное количество сердец
   if hearts_count > 10:
       hearts_count = 10
   if lost_hearts_count > 10:
       lost_hearts_count = 10

   # создаем строку с сердечками ми-ми-ми
   hearts_display = "♥" * hearts_count + "♡" * lost_hearts_count

   print(f"Начальное здоровье: {start_hp} HP")
   print(f"Ловушек: {traps_count} (урон: {trap_damage} HP)")
   print(f"Врагов: {enemies_count} (урон: {enemy_damage} HP)")
   print(f"Общий урон: {total_damage} HP")
   print(f"Оставшееся здоровье: {remaining_hp} HP")
   print(f"Здоровье: {hearts_display}")

   # ==================== ЗАДАНИЕ 1.7 ====================

   # замена символов на тупые смайлики
   print("\n=== Задание 1.7: Лабиринт с эмодзи ===")

   # новуая строка с заменой символов
   emoji_string = labyrinth_string

   # исп. метод replace() для замены символов на эмодзи
   emoji_string = emoji_string.replace("0", "⬜")  # проход
   emoji_string = emoji_string.replace("1", "⬛")  # стена
   emoji_string = emoji_string.replace("л", "🔷")  # ловушка
   emoji_string = emoji_string.replace("м", "🟡")  # монета
   emoji_string = emoji_string.replace("ф", "🟫")  # выход
   emoji_string = emoji_string.replace("з", "🐷")  # враг
   emoji_string = emoji_string.replace("н", "⭐")  # вход

   # вывод лабиринта с эмодзи
   print("Лабиринт с эмодзи:")
   for i in range(5):
       start_index = i * 5
       end_index = start_index + 5
       row = ""
       for j in range(5):
           char_index = start_index + j
           row += emoji_string[char_index]
       print(row)
# И ВСё!!1!!11


# ------------------------- TASK 2 -------------------------


# ЗАДАЧА 2: Симулятор фермы

print("=" * 50)
print("СИМУЛЯТОР ФЕРМЫ")
print("=" * 50)

# ==================== ЭТАП 1: База растений ====================
print("\n--- ЭТАП 1: База растений ---")
plants_input = input("Введите список растений (Название цвет размер рост, ...): ")
plants_list = plants_input.split(", ")

print("\nРастения на ферме:")
for plant in plants_list:
    print(plant)

# ==================== ЭТАП 2: Проверка возможности скрещивания ====================
print("\n--- ЭТАП 2: Проверка скрещивания ---")
hybrids_input = input("Введите список гибридов (формат: Роза+Тюльпан=Розотюльпан;...): ")

if hybrids_input.endswith(";"):
    hybrids_input = hybrids_input[:-1]

hybrid_rules = hybrids_input.split(";")

hybrid_dict = {}
for rule in hybrid_rules:
    if "=" not in rule:
        continue
    parents, child = rule.split("=")
    parent1, parent2 = parents.split("+")
    key = tuple(sorted([parent1.strip(), parent2.strip()]))
    hybrid_dict[key] = child.strip()

cross_input = input("Введите два названия растений для скрещивания (через пробел): ")
plant_a, plant_b = cross_input.split()
plant_a = plant_a.strip()
plant_b = plant_b.strip()

key = tuple(sorted([plant_a, plant_b]))
if key in hybrid_dict:
    print(f"Получен гибрид: {hybrid_dict[key]}")
else:
    print("Эти растения нельзя скрестить")

# ==================== ЭТАП 3: Определение свойств гибрида ====================
print("\n--- ЭТАП 3: Определение цвета, размера и скорости роста гибрида ---")

name1 = input("Введите название первого растения: ")
color1, size1, growth1 = input("Введите цвет, размер, скорость роста первого растения (через пробел): ").split()

name2 = input("Введите название второго растения: ")
color2, size2, growth2 = input("Введите цвет, размер, скорость роста второго растения (через пробел): ").split()

# 3.1 Определение цвета гибрида
if name1 < name2:
    hybrid_color = color1
elif name1 > name2:
    hybrid_color = color2
else:
    hybrid_color = color1

# 3.2 Определение размера гибрида

size_order = {"малый": 1, "средний": 2, "крупный": 3}
if size1 == size2:
    hybrid_size = size1
else:
    sizes = [size1, size2]
    sizes_sorted = sorted(sizes, key=lambda s: size_order.get(s, 0))
    hybrid_size = "/".join(sizes_sorted)

# 3.3 Определение скорости роста гибрида (наследует наименьшую скорость)

growth_order = {"медленный": 1, "средний": 2, "быстрый": 3}
if growth_order.get(growth1, 0) <= growth_order.get(growth2, 0):
    hybrid_growth = growth1
else:
    hybrid_growth = growth2

print("\nРезультаты для гибрида:")
print(f"Цвет: {hybrid_color}")
print(f"Размер: {hybrid_size}")
print(f"Скорость роста: {hybrid_growth}")

print("\nРабота программы завершена.")

























