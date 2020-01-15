"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
# цикл
num = int(input('Введите число: '))

new_num = ''
while num != 0:
    new_num += str(num % 10)
    num //= 10
print(new_num)


# Рекрусия

def inverse_number(numm , m):
    if numm == 0:
        return m
    else:
      return inverse_number(numm // 10, m * 10 + numm % 10)

numm = int(input("Введите число - "))
m = 0
print(f"Зеркальное число {inverse_number(numm,m)}")

