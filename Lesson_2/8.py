"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def count_with_series(numbers, check_num):
    count = 0
    for i in range(len(numbers)):
        div = str(1) + '0' * i
        div_shift = div + '0'
        if int(div) == 1:
            number = int(numbers) % 10
            if number == check_num:
                count += 1
        elif i + 1 == len(numbers):
            number = int(numbers) // int(div)
            if number == check_num:
                count += 1
        else:
            number = (int(numbers) % int(div_shift)) // int(div)
            if number == check_num:
                count += 1
    return count


row_num = input('Введите ряд чисел:')
num = int(input('Введите число, котрое нужно подсчитать:'))
print(count_with_series(row_num, num))