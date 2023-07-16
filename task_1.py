# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

hex_digits = "0123456789ABCDEF"
result = ""

num = int(input("Введите число: "))
x = num

print(f"{num} в шестнадцатиричной системе = {hex(num)[2:].upper()}")

while num > 0:
    digit = num % 16
    result = hex_digits[digit] + result
    num = num // 16
print(f"{x} в шестнадцатиричной системе = {result}")


