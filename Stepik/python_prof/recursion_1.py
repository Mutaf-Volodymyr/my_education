# Вам доступна функция traffic(), реализованная с помощью цикла while, которая принимает в качестве аргумента число
# n и выводит n раз строку Не парковаться.
# Перепишите данную функцию с использованием рекурсии, чтобы она выполняла ту же задачу.

# def traffic(n):
#     if n > 0:
#         print('Не парковаться')
#         traffic(n - 1)


###############################################
# Напишите программу с использованием рекурсии, которая выводит последовательность натуральных
# чисел от 1 до 100 включительно.
# def traffic():
#     def res(n):
#         if n <= 100:
#             print(n)
#             res(n + 1)
#     res(1)
#
# traffic()

###############################################
# Вам доступен список numbers, содержащий ровно 100 целых чисел. Дополните приведенный ниже код с использованием рекурсии,
# чтобы он вывел все элементы этого списка от первого до последнего, каждый на отдельный строке, в следующем формате:
# Элемент <индекс элемента>: <значение элемента>

# def recursion(n):
#     n_len = len(n)
#     def print_element(index_now):
#         if index_now < n_len:
#             print(f'Элемент {index_now}: {n[index_now]}')
#             print_element(index_now + 1)
#     print_element(0)
#
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432,
#            -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232,
#            755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728,
#            558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762,
#            -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
# recursion(numbers)


###############################################
# Дана последовательность целых чисел. Напишите программу с использованием рекурсии, которая выводит эту последовательность в обратном порядке.
# Формат входных данных
# На вход программе подается последовательность целых чисел, каждое на отдельной строке. Концом последовательности является число 0

# def recursion_1():
#     n = int(input())
#     if n != 0:
#         recursion_1()
#     print(n)
#
# recursion_1()

###############################################
# Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:
#     h — натуральное число
# Функция должна выводить звездный треугольник с высотой h

# def triangle(h):
#     print('*' * h)
#     if h > 1:
#         triangle(h-1)

###############################################
# Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:
# h — натуральное число
# Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:

# def triangle(h):
#     if h >= 1:
#         triangle(h-1)
#         print('*' * h)
#
# triangle(5)

###############################################
# Напишите программу с использованием рекурсивной функции, которая выводит изображение песочных часов, составленное из цифр
#
# 1111111111111111    # 16 раз
#   222222222222      # 12 раз
#     33333333        # 8 раз
#       4444          # 4 раза
#     33333333        # 8 раз
#   222222222222      # 12 раз
# 1111111111111111    # 16 раз


# def hourglass():
#     m, row = 4, 20
#     def hour_gl(n):
#         p = str(n) * (row - (m*n))
#         if m != n:
#             print(p.center(m ** 2, ' '))
#             hour_gl(n+1)
#         print(p.center(m ** 2, ' '))
#     hour_gl(1)
#
#
# hourglass()

###############################################
# Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.

# def print_digits(number):
#     if number != 0:
#         print(number % 10)
#         number = number // 10
#         print_digits(number)
#


###############################################
# Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
# number — натуральное число
# Функция должна выводить все цифры числа number, начиная со старших разрядов, каждое на отдельной строке.

# def print_digits(number):
#     if number != 0:
#         print_digits(number // 10)
#         print(number % 10)
#
# print_digits(1234567)


###############################################
# Напишите программу с использованием рекурсии, которая принимает на вход число и выводит количество цифр в этом числе.

# def num_of_digits(number):
#     if number < 10:
#         return 1
#     return 1 + num_of_digits(number // 10)
#
# print(num_of_digits(int(input())))


###############################################
# Напишите программу с использованием рекурсии, которая принимает на вход число и выводит сумму цифр этого числа.

# def num_of_digits(number):
#     if number < 10:
#         return number % 10
#     return number % 10 + num_of_digits(number // 10)
#
# print(num_of_digits(int(input())))


###############################################
# В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся
# размножаются, и их становится в три раза больше.
# Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:
#     year — натуральное число
# Функция должна возвращать единственное число — количество лягушек в пруду в году year.

# def number_of_frogs(year):
#     if year == 1:
#         return 77
#     else:
#         return (number_of_frogs(year-1) - 30) * 3
#
# print(number_of_frogs(int(input())))

###############################################
# Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:
#     numbers — список целых чисел
#     start — целое неотрицательное число
#     end — целое неотрицательное число
# Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно и возвращать полученный результат.

# def range_sum(numbers, start, end):
#     if start == end:
#         return numbers[end]
#     else:
#         return numbers[start] + range_sum(numbers, start+1, end)
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))


###############################################
# Реализуйте функцию get_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
#
    # a — положительное целое число
    # n — неотрицательное целое число
# Функция должна вычислять значение a в степени n и возвращать полученный результат.

# def get_pow(a, n):
#     if n == 0:
#         return 1
#     return a * get_pow(a, n-1)
#
#
# print(get_pow(2, 10))

###############################################
# Возводить в степень можно гораздо быстрее, чем за n умножений.
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:

# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         return get_fast_pow(a * a, n // 2)
#     else:
#         return a * get_fast_pow(a, n-1)


###############################################
# Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
#
#     nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
# также являются либо целые числа, либо списки; вложенность может быть произвольной
# Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
# Если список nested_lists пуст, функция должна вернуть число 0.

################### РАБОТАЕТ ############################
# def recursive_sum(data):
#     total = []
#     def recursive(data1):
#         if type(data1) == int:
#             total.append(data1)
#         elif type(data1) == list:
#             for i in data1:
#                 recursive(i)
#     recursive(data)
#     return sum(total)

####### НЕ ПОНИМАЮ ПОЧЕМУ Я НЕ МОГУ ПОЛУЧИТЬ ДОСТУП К ПЕРЕМЕННОЙ (теперь понимаю)#######
# def recursive_sum(data):
#     total = 0
#     def recursive(data1):
#         nonlocal total
#         if type(data1) == int:
#             total += data1
#         elif type(data1) == list:
#             for i in data1:
#                 recursive(i)
#     recursive(data)
#     return total

############# РАБОТАЕТ #####################
# def recursive_sum(data):
#     total = 0
#     for el in data:
#         if type(el) == int:
#             total += el
#         elif type(el) == list:
#             total += recursive_sum(el)
#     return total

#
# my_list = [1, [4, 4], 2, [1, [2, 10]]]
#
# print(recursive_sum(my_list))


###############################################
# Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:
#
# nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
# Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.
#
# def linear(nested_lists):
#     total = []
#     def recursive(data1):
#         if type(data1) == int:
#             total.append(data1)
#         elif type(data1) == list:
#             for i in data1:
#                 recursive(i)
#     recursive(nested_lists)
#     return total
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))


###############################################
# Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:
# nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь,
# так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    # key — хешируемый объект
# Функция должна определять значение, которое соответствует ключу key в словаре nested_dicts или в одном из его
# вложенных словарей, и возвращать полученный результат.

# def get_value(nested_dicts, key):
#     if key in nested_dicts:
#         return nested_dicts[key]
#     for i in nested_dicts.values():
#         if isinstance(i, dict):
#             value = get_value(i, key)
#             if value is not None:
#                 return value
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))


###############################################
# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
    # nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые,
# в свою очередь, так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    # key — хешируемый объект
# Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных словарях, и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое множество.
#
# def get_all_values(nested_dicts, key):
#     res = set()
#     def get_value(nested_dicts, key):
#         if key in nested_dicts:
#             res.add(nested_dicts[key])
#         for i in nested_dicts.values():
#             if isinstance(i, dict):
#                 value = get_value(i, key)
#                 if value is not None:
#                     return value
#     get_value(nested_dicts, key)
#     return res
#
#
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(*sorted(result))



# Реализуйте функцию dict_travel(), которая принимает один аргумент:
#
# nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь,
# так же содержат в качестве значений числа, строки или словари; вложенность может быть произвольной
# Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
# При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, разделяя их точками.


# def dict_travel(nested_dicts, path=[]):
#
#     for k, v in sorted(nested_dicts.items()):
#         if isinstance(v, dict):
#             dict_travel(v, path + [k])
#         else:
#             print(f"{'.'.join(path + [k])}: {v}")








# Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
#
# a — неотрицательное целое число
# b — неотрицательное целое число
# Функция должна возвращать сумму чисел a и b. При вычислении суммы функция:
#
# не должна использовать циклы
# из всех арифметических операций должна использовать только +1 и −1


# def recursive_sum(a, b, count = 0):
#     if a > b:
#         a, b = b, a
#     if count == b:
#         return a
#     else:
#         return recursive_sum(a+1, b, count + 1)
#
# print(recursive_sum(10, 22))



# Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.

# def is_power(number):
#     if number == 1:
#         return True
#     elif number % 2 != 0:
#         return False
#     else:
#         return is_power(number / 2)
#
#
# print(is_power(512))
#
# print(is_power(15))


# Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:

# 1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …
#
# Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
#
# n — натуральное число
# Функция должна возвращать n-й член последовательности Трибоначчи.

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def tribonacci(n):
#     if n <= 3:
#         return 1
#     else:
#         return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

# Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.

# def is_palindrome(string):
#     if len(string) <= 1:
#         return True
#     elif string[0] != string[-1]:
#         return False
#     else:
#         return is_palindrome(string[1:-1])



# Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
#
# number — неотрицательное целое число
# Функция должна возвращать строковое представление числа number в двоичной системе счисления.

# def to_binary(number):
#     if number <= 1:
#         return str(number)
#     return to_binary(number // 2) + str(number % 2)



# Напишите программу с использованием рекурсии, которая принимает на вход число n и вычитает из него число  5,
# пока оно не перестанет быть положительным, а затем прибавляет к нему число  5, пока оно снова не станет равным # n.

# def recursion_1(n):
#     if n <= 0:
#         print(n)
#     else:
#         print(n)
#         recursion_1(n-5)
#         print(n)
#
# recursion_1(int(input()))