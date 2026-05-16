# ------------------------- TASK 1 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Шумоподавление ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

words_str = input("Введите слова через пробел: ")
unique_words = set(words_str.split())

print(f"Количество: {len(unique_words)}")
print("Слова:", *sorted(unique_words))


# ------------------------- TASK 2 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                  Контроль доступа ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

allowed_str = input("Введите разрешённые ID через пробел: ")
allowed_set = set(allowed_str.split())

# ввод входящих ID
incoming_str = input("Введите входящие ID через пробел: ")
incoming_list = incoming_str.split()

# иииии обработка каждого входящего ID
for id_ in incoming_list:
   if id_ in allowed_set:
       print("OK")
   else:
       print("ADDED")
       allowed_set.add(id_)


# ------------------------- TASK 3 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                  Сверка серверов ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

a_str = input("Сервер A (файлы через пробел): ")
set_a = set(a_str.split())

b_str = input("Сервер B (файлы через пробел): ")
set_b = set(b_str.split())

# общие файлы (пересечение)
common = set_a & set_b
# потерянные файлы
lost = set_a - set_b

print("Общие:", *sorted(common))
print("Потерянные:", *sorted(lost))


# ------------------------- TASK 4 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                  Двойной агент ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

cia_str = input("ЦРУ (имена через пробел): ")
cia_set = set(cia_str.split())

mi6_str = input("МИ-6 (имена через пробел): ")
mi6_set = set(mi6_str.split())

kgb_str = input("КГБ (имена через пробел): ")
kgb_set = set(kgb_str.split())

double_agents = (cia_set & mi6_set) - kgb_set

print(*sorted(double_agents, reverse=True))


# ------------------------- TASK 5 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("             Подозрительная активность ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

log1_str = input("Лог 1 (IP через пробел): ")
set1 = set(log1_str.split())

log2_str = input("Лог 2 (IP через пробел): ")
set2 = set(log2_str.split())

log3_str = input("Лог 3 (IP через пробел): ")
set3 = set(log3_str.split())

in_all = set1 & set2 & set3
all_ips = set1 | set2 | set3
result = all_ips - in_all

print(*sorted(result))


# ------------------------- TASK 6 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Призрак в сети ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

dept1_str = input("Отдел 1 (числа через пробел): ")
dept1_set = set(map(int, dept1_str.split()))

dept2_str = input("Отдел 2 (числа через пробел): ")
dept2_set = set(map(int, dept2_str.split()))

dept3_str = input("Отдел 3 (числа через пробел): ")
dept3_set = set(map(int, dept3_str.split()))

full_set = set(range(11))
present = dept1_set | dept2_set | dept3_set
ghosts = full_set - present

print(*sorted(ghosts))


# ------------------------- TASK 7 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Точка эвакуации ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

agent = (2, 2)

points = {(1, 1), (5, 5), (0, 3)}

def manhattan(p1, p2):
   return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

closest = min(points, key=lambda p: manhattan(p, agent))

print("Ближайшая точка к агенту:", closest)

