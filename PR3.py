# ------------------------- TASK 1 -------------------------

print("Типы переменных:")


a = 42
print(f"a = {a}, type(a) = {type(a)}")


b = 3.14159
print(f"b = {b}, type(b) = {type(b)}")


c = "Hello, Python!"
print(f"c = {c}, type(c) = {type(c)}")


d = True
print(f"d = {d}, type(d) = {type(d)}")


e = [1, 2, 3]
print(f"e = {e}, type(e) = {type(e)}")


f = (4, 5, 6)
print(f"f = {f}, type(f) = {type(f)}")


g = {"name": "Alice", "age": 30}
print(f"g = {g}, type(g) = {type(g)}")


h = {7, 8, 9}
print(f"h = {h}, type(h) = {type(h)}")


i = None
print(f"i = {i}, type(i) = {type(i)}")


# ------------------------- TASK 2 -------------------------

# 1. Список (изменяемый)
my_list = [1, 2, 3]
print(f"Исходный список: {my_list}")
my_list[0] = 100
print(f"После изменения: {my_list}")
print("Список является ИЗМЕНЯЕМЫМ - т.к. мы можем менять его элементы")


# 2. Кортеж (неизменяемый)
my_tuple = (1, 2, 3)
print(f"\nИсходный кортеж: {my_tuple}")
print("Кортеж является НЕИЗМЕНЯЕМЫМ - т.к. нельзя менять его элементы")
print("При попытке изменить элемент кортежа возникнет ошибка TypeError")


# 3. Строка (неизменяемый)
my_string = "cat"
print(f"\nИсходная строка: {my_string}")
print("Строка является НЕИЗМЕНЯЕМОЙ - т.к. нельзя менять отдельные символы")
print("При попытке изменить символ строки возникнет ошибка TypeError")

# ------------------------- TASK 3 -------------------------

num1_str = input("Введите первое число: ")
num2_str = input("Введите второе число: ")


num1 = int(num1_str)
num2 = int(num2_str)


result = num1 + num2
print(result)


try:
   num1_str = input("Введите первое число: ")
   num2_str = input("Введите второе число: ")


   num1 = int(num1_str)
   num2 = int(num2_str)


   result = num1 + num22
   print(result)


except ValueError:
   print("Ошибка! Вводите только целые числа.")


# ------------------------- TASK 4 -------------------------

""" В гугл docx """

# ------------------------- TASK 5 -------------------------

shopping_list = ["хлеб", "молоко", "яйца", "сыр"]
shopping_list.append("фрукты")
print(len(shopping_list))


unique_items = set(shopping_list)
print(unique_items)

# ------------------------- TASK 6 -------------------------

print("=== Анкета студента ===")


# запрашиваем данные у пользователя чтобы далее их использовать
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
facult = input("Введите ваш факультет: ")
course = input("Введите ваш курс: ")
hobbi = input("Введите ваши увлечения (через запятую, пожалуйста): ")


# возраст в число
try:
   age = int(age)
   course = int(course)
except ValueError:
   print("Ошибка ввода возраста или курса!")
   exit()


# разделяем увлечения в список
hobbi_list = [hobbi.strip() for hobbi in hobbi.split(',')]


# создаем лист с данными чела
prof = {
   "имя": name,
   "возраст": age,
   "факультет": facult,
   "курс": course,
   "увлечения": hobbi_list
}


# Итог
print("\n=== Ваша анкета ===")
for key, value in prof.items():
   print(f"{key.capitalize()}: {value}")





