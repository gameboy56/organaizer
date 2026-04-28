import random

# ----------------------------------------------------------------------
# вспомогательная функция для генерации случайного вложенного списка
# ----------------------------------------------------------------------

def generate_nested_list(rows=4, cols=3, min_val=-10, max_val=20):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# ----------------------------------------------------------------------
# задача 1. поиск максимального элемента и его позиции
# ----------------------------------------------------------------------


def task1(nested_list):
    if not nested_list or not nested_list[0]:
        return None, None

    max_val = nested_list[0][0]
    max_row = 0
    max_col = 0

    # перебор всех элементов с помощью вложенных циклов
    for i, row in enumerate(nested_list):
        for j, val in enumerate(row):
            if val > max_val:
                max_val = val
                max_row = i
                max_col = j

    return max_row, max_col, max_val


# ----------------------------------------------------------------------
# задача 2. подсчёт суммы элементов каждого подсписка и общей суммы
# ----------------------------------------------------------------------


def task2(nested_list):
    sums = []               # это список сумм по строкам
    total_sum = 0
    max_sum = float('-inf')
    max_row_index = -1

    for i, row in enumerate(nested_list):
        row_sum = sum(row)
        sums.append(row_sum)
        total_sum += row_sum

        if row_sum > max_sum:
            max_sum = row_sum
            max_row_index = i

    return sums, total_sum, max_row_index, max_sum


# ----------------------------------------------------------------------
# задача 3. фильтрация вложенного списка (оставить только положительные элементы)
# ----------------------------------------------------------------------


def task3(nested_list):
    filtered = []
    for row in nested_list:
        # Оставляем только положительные числа в строке
        positive_row = [x for x in row if x > 0]
        filtered.append(positive_row)
    return filtered


# ----------------------------------------------------------------------
# задача 4. поиск всех позиций заданного элемента во вложенном списке
# ----------------------------------------------------------------------


def task4(nested_list, target):
    positions = []
    for i, row in enumerate(nested_list):
        for j, val in enumerate(row):
            if val == target:
                positions.append((i, j))
    return positions


# ----------------------------------------------------------------------
# задача 5. лут в рейде (максимальная сумма N предметов)
# ----------------------------------------------------------------------


def task5():
    try:
        N = int(input("Введите количество предметов, которые можно унести (N): "))
        values_input = input("Введите ценности предметов через пробел: ")
        values = list(map(int, values_input.split()))
    except ValueError:
        print("Ошибка ввода. Используйте целые числа.")
        return

    # решение: сортируем по убыванию и берём первые N
    # если N больше длины списка, берём все
    if N <= 0:
        print("Максимальная сумма: 0")
        return

    sorted_values = sorted(values, reverse=True)
    taken = sorted_values[:N]
    max_sum = sum(taken)
    print(f"Максимальная возможная суммарная ценность: {max_sum}")


# ----------------------------------------------------------------------
# задача 6. Разгребаем инвентарь (4 вида сортировки/порядка)
# ----------------------------------------------------------------------


def task6():
    try:
        items_input = input("Введите цены предметов через пробел: ")
        items = list(map(int, items_input.split()))
    except ValueError:
        print("Ошибка ввода. Используйте целые числа.")
        return

    # 1. сортировка по возрастанию
    asc = sorted(items)
    # 2. сортировка по убыванию
    desc = sorted(items, reverse=True)
    # 3. оригинальный порядок (как были введены)
    original = items.copy()
    # 4. обратный порядок (от новых к старым)
    reversed_order = items[::-1]

    # вывод в требуемом формате
    print(f"Сортировка по возрастанию: {asc}")
    print(f"Сортировка по убыванию: {desc}")
    print(f"Оригинальный порядок (от старых к новым): {original}")
    print(f"Обратный порядок (от новых к старым): {reversed_order}")


# ----------------------------------------------------------------------
# Задача 7. Сортировка пузырьком с циклом while и флагом оптимизации
# ----------------------------------------------------------------------


def bubble_sort_while(arr):
    n = len(arr)
    if n <= 1:
        return arr

    i = 0
    while i < n - 1:
        swapped = False
        j = 0
        # проходим по несортированной части
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1
        # если не было обменов, массив уже отсортирован
        if not swapped:
            break
        i += 1
    return arr


# ----------------------------------------------------------------------
# Задача 8. Сортировка выбором с циклом while
# ----------------------------------------------------------------------


def selection_sort_while(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        # находим индекс минимального элемента в оставшейся части
        min_idx = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        # меняем местами
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    return arr

# ----------------------------------------------------------------------
# Демонстрация работы всех задач
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 50)
    print("Практическое занятие №14 - Обработка вложенных списков и сортировка")
    print("=" * 50)

    # генерируем один вложенный список для задач 1-4
    nested = generate_nested_list(rows=4, cols=3, min_val=-10, max_val=20)
    print("\nСгенерированный вложенный список:")
    for row in nested:
        print(row)

    # задача 1
    print("\n--- Задача 1 ---")
    row_idx, col_idx, max_val = task1(nested)
    print(f"Максимальный элемент: {max_val} находится на позиции: строка {row_idx}, столбец {col_idx}")

    # задача 2
    print("\n--- Задача 2 ---")
    sums, total, max_row, max_sum = task2(nested)
    print(f"Суммы строк: {sums}")
    print(f"Общая сумма всех элементов: {total}")
    print(f"Строка с максимальной суммой: индекс {max_row}, сумма = {max_sum}")

    # задача 3
    print("\n--- Задача 3 ---")
    filtered_list = task3(nested)
    print("Исходный список:")
    for row in nested:
        print(row)
    print("Отфильтрованный список (только положительные):")
    for row in filtered_list:
        print(row)

    # задача 4
    print("\n--- Задача 4 ---")
    # ищем случайный элемент, который есть в списке, например, первое число из первой строки
    target = nested[0][0] if nested else 0
    positions = task4(nested, target)
    print(f"Позиции элемента {target}: {positions}")

    # задача 5 (интерактивный ввод)
    print("\n--- Задача 5 ---")
    task5()

    # задача 6 (интерактивный ввод)
    print("\n--- Задача 6 ---")
    task6()

    # задача 7
    print("\n--- Задача 7. (Сортировка пузырьком с while) ---")
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", test_list)
    sorted_bubble = bubble_sort_while(test_list.copy())
    print("Отсортированный пузырьком:", sorted_bubble)

    # задача 8
    print("\n--- Задача 8. (Сортировка выбором с while) ---")
    test_list2 = [64, 25, 12, 22, 11]
    print("Исходный список:", test_list2)
    sorted_selection = selection_sort_while(test_list2.copy())
    print("Отсортированный выбором:", sorted_selection)




























