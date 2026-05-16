import math

# ------------------------- TASK 1 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("              Количество дней в месяце ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def get_days(month):
   if month in [1, 3, 5, 7, 8, 10, 12]:
       return 31
   elif month == 2:
       return 28
   elif month in [4, 6, 9, 11]:
       return 30
   else:
       return "Ошибка: Месяц не найден"

user_pishet = int(input("Введите номер месяца (1-12): "))
print(f"Количество дней: {get_days(user_pishet)}")


# ------------------------- TASK 2 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Проверка чисел ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def is_prime(num):
  if num <= 1:
      return False


  for i in range(2, int(num ** 0.5) + 1):
      if num % i == 0:
          return False
  return True

print("       Натуральное число - это False")
print("         Простое число - это True")
print("---------------------------------------------")

n = int(input("Проверка списка чисел: "))

if is_prime(n):
   print("""""""""""""""""""""""")
   print(f"Число {n} - простое (True)")
else:
   print("""""""""""""""""""""""")
   print(f"Число {n} - Натуральное (False)")


# ------------------------- TASK 3 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Next Prime  ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def get_next_prime(num):
   next_num = num + 1
   while True:
       is_prime = True
       if next_num < 2:
           is_prime = False
       else:
           for i in range(2, int(next_num ** 0.5) + 1):
               if next_num % i == 0:
                   is_prime = False
                   break

       if is_prime:
           return next_num
       next_num += 1

n = int(input("Введите число: "))
result = get_next_prime(n)
print(result)


# ------------------------- TASK 4 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Good password  ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def is_password_good(password):

   if len(password) < 8:
       return False

   has_upper = False
   has_lower = False
   has_digit = False

   for char in password:
       if char.isupper():
           has_upper = True
       elif char.islower():
           has_lower = True
       elif char.isdigit():
           has_digit = True

   return has_upper and has_lower and has_digit

user_password = input("Введите пароль: ")
result = is_password_good(user_password)
print(result)


# ------------------------- TASK 5 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                      Пчел Гик  ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def is_valid_password(password):
   parts = password.split(':')

   if len(parts) != 3:
       return False

   a, b, c = parts
   if not (a.isdigit() and b.isdigit() and c.isdigit()):
       return False

   num_b = int(b)
   num_c = int(c)
   if a != a[::-1]:
       return False
   if num_b < 2:
       return False
   for i in range(2, int(num_b ** 0.5) + 1):
       if num_b % i == 0:
           return False

   if num_c % 2 != 0:
       return False

   return True

user_input = input("Введите пароль в формате a:b:c: ")
result = is_valid_password(user_input)
print(result)


# ------------------------- TASK 6 -------------------------


# Design программы
print("""""""""""""""""""""""")
print("     )----------------------------------------(")
print("                   Корни уравнения  ")
print("     )----------------------------------------(")
print("""""""""""""""""""""""")

def solve(a, b, c):
    d = b**2 - 4 * a* c
    sqrt_d = math.sqrt(d)

    x1 = (-b - sqrt_d) / (2*a)
    x2 = (-b + sqrt_d) / (2*a)

    if x1 < x2:
        return x1, x2
    else:
        return x2, x1

if __name__ == "__main__":
    a = int(input("Введите коэффициент a: "))
    b = int(input("Введите коэффициент b: "))
    c = int(input("Введите коэффициент c: "))

    root1, root2 = solve(a, b, c)

    print("""""""""""""""""""""""")
    print("Вывод: ", "x1:", root1, "| x2:", root2)













