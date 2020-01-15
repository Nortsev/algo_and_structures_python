"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def calc_sum(n, s=0):
    if n == 0:
        return s
    else:
        return calc_sum(n // 10, s + (n % 10))


nums = input("Введите последовательность чисел, разделённых пробелами: ")
max_sum = 0
max_num = 0

for num in nums.split():
    n_sum = calc_sum(abs(int(num)))
    if n_sum > max_sum:
        max_sum = n_sum
        max_num = num

print(f"Максимальное число по сумме цифр: {max_num} сумма цифр {max_sum}")