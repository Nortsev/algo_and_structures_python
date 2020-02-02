"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import collections

input_str = 'Welcome to geekbrains development'
str_count = collections.Counter()
list_str = list(input_str)
for i in list_str:
    str_count[i] += 1

list_letter = list(map(list, sorted(list(str_count.items()), key=lambda count: count[1])))
list_val = [i[0] for i in list_letter]


def tree_building(list_input):
    dict_tree = {}
    for i in range(len(list_input) - 1):
        count = list_input[i][1] + list_input[i + 1][1]
        list_input[i][1], list_input[i + 1][1] = 0, 1
        dict_tree[f'root_{i}'] = {list_input[i][0]: list_input[i][1], list_input[i + 1][0]: list_input[i + 1][1]}
        list_input[i][0], list_input[i][1] = f'root_{i}', count
        list_input = sorted(list_input, key=lambda count: count[1])
    return dict_tree


def find_val(val_find, dict_input):
    list_res = []
    for i in dict_input:
        if val_find in dict_input[i]:
            list_res.append([dict_input[i][val_find], i])
    return list_res


def bin_code(val_bin, dict_input):
    list_res = []
    while True:
        temp = find_val(val_bin, dict_input)
        if not (temp):
            break
        list_res.append(str(temp[0][0]))
        val_bin = temp[0][1]
    list_res.reverse()
    return list_res


def res_bin_dict(list_input, dict_input):
    dict_bin_code = {}
    for i in list_input:
        dict_bin_code[i] = f"{''.join(bin_code(i, dict_input))}"
    return dict_bin_code


dict_tree = tree_building(list_letter)
dict_code = res_bin_dict(list_val, dict_tree)
list_code_str = [dict_code[i] for i in list_str]

print(f'Исходная строка: {input_str}')
print(f"Закодированная строка: {''.join(list_code_str)}")