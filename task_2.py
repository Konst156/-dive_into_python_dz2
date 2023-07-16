# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

fraction_1 = input("Введите первую дробь: ")
fraction_2 = input("Введите вторую дробь: ")

num1, denom1 = map(int, fraction_1.split('/'))
num2, denom2 = map(int, fraction_2.split('/'))
common_denom = denom1 * denom2  # Находим общий знаменатель
sum_num = num1 * denom2 + num2 * denom1  # Вычисляем числитель для суммы
product_num = num1 * num2  # Вычисляем числитель для произведения


def find_gcd(a, b): # сокращение дроби (поиск общего делителя)
    while b != 0:
        a, b = b, a % b
    return a


print(
    f"Сумма дробей = {int(sum_num / find_gcd(sum_num, common_denom))}/{int(common_denom / find_gcd(sum_num, common_denom))}")
print(
    f"Произведение дробей = {int(product_num / find_gcd(product_num, common_denom))}/{int(common_denom / find_gcd(product_num, common_denom))}")

# Проверка
# Вычисляем сумму дробей
sum_frac = Fraction(fraction_1) + Fraction(fraction_2)
# Вычисляем произведение дробей
product_frac = Fraction(fraction_1) * Fraction(fraction_2)

print(f"Сумма: {str(sum_frac)}")
print(f"Произведение: {str(product_frac)}")
