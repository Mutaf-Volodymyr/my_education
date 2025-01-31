##############################################
# Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.
# Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность
# натуральных чисел, в которой каждое число встречается столько раз, каково оно:
from os.path import getsize

# def simple_sequence():
#     n = 1
#     while True:
#         for _ in range(n):
#             yield n
#         n += 1
#
# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]
#
# print(*numbers)

##############################################
# Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:
#
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный
# знакочередующийся ряд натуральных чисел.
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
# порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.

# def alternating_sequence(count=None):
#     n = 1
#     while count != 0:
#         if count is not None:
#             count -= 1
#         yield n if n % 2 else -n
#         n += 1


##############################################
# Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
# left — натуральное число
# right — натуральное число
# Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно,
# а затем возбуждающий исключение StopIteration.

# def primes(left, right):
#     for i in range(left, right+1):
#         if i == 1:
#             continue
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             yield i


##############################################

# Реализуйте генераторную функцию reverse(), которая принимает один аргумент:
#
# sequence — последовательность
# Функция должна возвращать генератор, порождающий элементы последовательности
# sequence в обратном порядке, а затем возбуждающий исключение StopIteration.

# def reverse(sequence):
#     yield from reversed(sequence)




##############################################
# Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:
# start — дата, тип date
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность
# из максимально допустимого количества дат (тип date), начиная с даты start.
# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
# порождающий последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

# from datetime import date, timedelta
# def dates(start, count=None):
#     while count != 0:
#         if count is not None:
#             count -= 1
#         yield start
#         if start == date.max:         # PEP 479 – Change StopIteration handling inside generators
#             return StopIteration      # raise StopIteration - not work
#         start += timedelta(days=1)
#
#
#
# generator = dates(date(9999, 1, 7))
# for _ in range(348):
#     next(generator)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# try:
#    print(next(generator))
# except StopIteration:
#     print('Error')

##############################################
# Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:
#
# suit — одна из четырех карточных мастей: пик, треф, бубен, червей
# Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit.
# Каждая карта должна представлять собой строку в следующем формате:

# def card_deck(suit):
#     nominee =  ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
#     mast = ['пик', 'треф', 'бубен', 'червей']
#     mast.remove(suit)
#     mast_index, nominee_index = 0, 0
#     while True:
#         if nominee_index > 12:
#             mast_index += 1
#             nominee_index = 0
#         if mast_index == 3:
#             mast_index = 0
#             nominee_index = 0
#         yield f'{nominee[nominee_index]} {mast[mast_index]}'
#         nominee_index += 1



##############################################
# Вам доступна генераторная функция matrix_by_elem(), которая принимает в качестве аргумента матрицу
# произвольной размерности и возвращает генератор, порождающий последовательность элементов переданной матрицы.
#
# Перепишете данную функцию с использованием конструкции yield from, чтобы она выполняла ту же задачу.

# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row


##############################################

# Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.
# Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

# def palindromes():
#     n = 0
#     while True:
#         n += 1
#         if str(n) == str(n)[::-1]:
#             yield n


##############################################
# Реализуйте генераторную функцию flatten(), которая принимает один аргумент:
    # nested_list — список, элементами которого являются целые числа или списки, элементами которых,
# в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
# Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list,
# включая все числа из всех вложенных списков, а затем возбуждает исключение StopIteration.

# def flatten(nested_list):
#     for el in nested_list:
#         if isinstance(el, list):
#             yield from flatten(el)
#         else: yield el


##############################################
# Вам доступна генераторная функция cubes_of_odds(), принимающая в качестве аргумента итерируемый объект,
# элементами которого являются целые числа, и возвращающая генератор, порождающий последовательность нечетных
# чисел переданного итерируемого объекта, возведенных в третью степень.
#
# Перепишите данную функцию с использованием генераторного выражения, чтобы она выполняла ту же задачу.

# def cubes_of_odds(iterable):
#     yield from (i**3 for i in iterable if i % 2)



##############################################
# Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:
#
# number — натуральное число
# Функция должна возвращать True, если число number является простым, или False в противном случае.

# def is_prime(number):
#     if number != 1:
#         return all(number % i for i in range(2, number))
#     return False

##############################################
# Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:
    # iterable — итерируемый объект
# Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

# def count_iterable(iterable):
#     return sum(1 for _ in iterable)


##############################################
# Реализуйте функцию all_together() с использованием генераторных выражений, которая принимает произвольное
# количество позиционных аргументов, каждый из которых является итерируемым объектом.
#
# Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов:
# сначала все элементы первого итерируемого объекта, затем второго, и так далее.

# def all_together(*args):
#     return (i for row in args for i in row)
#
# objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]


##############################################
# Реализуйте функцию interleave() с использованием генераторных выражений, которая принимает
# произвольное количество позиционных аргументов, каждый из которых является последовательностью.
# Функция должна возвращать генератор, порождающий каждый элемент всех переданных последовательностей:
# сначала первый элемент первой последовательности, затем первый элемент второй последовательности, и так далее;
# после второй элемент первой последовательности, затем второй элемент второй последовательности, и так далее.


# def interleave(*args):
#     return (i for row in zip(*args) for i in row)

##############################################
# Вам доступен именованный кортеж Person, который содержит данные о человеке.
# Первым элементом именованного кортежа является имя и фамилия человека, вторым — национальность,
# третьим — пол, четвертым — год рождения, пятым — год смерти. Если человек жив, год смерти считается равным 0.
# Также доступен список persons, содержащий эти кортежи.
# Дополните приведенный ниже код с использованием конвейеров генераторов, чтобы он вывел имя и фамилию
# самого молодого живого мужчины (male) из Швеции (Swedish).

#
# from collections import namedtuple
#
# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
#
# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
#
# live = (i for i in persons if i.death == 0)
# sex = (i for i in live if i.sex == 'male')
# nationality = (i for i in sex if i.nationality == 'Swedish')
#
# print(max(nationality, key=lambda x: x.birth).name)


##############################################
# Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница диапазона,
# причем a <= b. Диапазон содержит в себе все числа от a до b включительно.
# Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:
#
# ranges — строка, в которой через запятую указаны диапазоны чисел
# Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.

# def parse_ranges(ranges):
#     a = (i.split('-') for i in ranges.split(','))
#     for i in a:
#         yield from range(int(i[0]), int(i[1])+1)


##############################################
# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
#
    # names — список имен
    # ignore_char — одиночный символ
    # max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
#
# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка.

# def filter_names(names, ignore_char, max_names):
#     a = (i for i in names if not i[0].lower() in ignore_char.lower())
#     b = (i for i in a if i.isalpha())
#     yield from (el for i, el in enumerate(b) if i < max_names)



##############################################
# Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы.
# В первом столбце записано название компании (стартапа), во втором — инвестируемая сумма в долларах,
# в третьем — раунд инвестиции.


# with open('generator_1/data.csv', 'r', encoding='utf-8') as f:
#     next(f)
#     line_values = (line.rstrip().split(',') for line in f)
#     round_a = (int(b) for a, b, s in line_values if s == 'a')
#     print(sum(round_a))

##############################################
# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
# year — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

# from datetime import date, timedelta
# def years_days(year):
#     first_day = date(year, 1, 1)
#     while first_day.year == year:
#         yield first_day
#         first_day += timedelta(days=1)


##############################################
# Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
#
# file — название текстового файла, например, data.txt
# Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с
# убранным символом переноса строки \n. Если строка содержит более
# 25 символов, она заменяется многоточием ....

# def nonempty_lines(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         yield from (l.rstrip() if len(l) <= 27 else '...' for l in f if not l.isspace())
#
# print(*nonempty_lines('generator_1/test.txt'), sep='\n')

##############################################

# Вам доступен файл planets.txt, содержащий информацию о различных планетах.
# В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка,
# затем характеристики второй планеты, и так далее:
# Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.
# Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых
# содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период.

# def txt_to_dict():
#     with open('generator_1/planets.txt', 'r', encoding='utf8') as f:
#         a = [i.split('\n') for i in f.read().split('\n\n')]
#         p = ' ='
#         b = ({n.split()[0]: n.split(p)[1].strip(),
#               d.split(p)[0]: d.split(p)[1].strip(),
#               m.split(p)[0]: m.split(p)[1].strip(),
#               o.split(p)[0]: o.split(p)[1].strip()
#               } for n, d, m, o in a)
#
#         yield from b


##############################################
# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.

# def unique(iterable):
#     a = set()
#     for i in iterable:
#         if i not in a:
#             yield i
#             a.add(i)



##############################################
# Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:
# iterable — итерируемый объект
# obj — произвольный объект
# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого
# объекта iterable до тех пор, пока не будет достигнут элемент, равный obj. Если итерируемый объект
# iterable не содержит ни одного элемента, равного obj, генератор должен породить все элементы iterable.

# def stop_on(iterable, obj):
#     it = iter(iterable)
#     return iter(lambda: next(it), obj)





##############################################
# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей,
# каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предшествующий ему элемент:
# (<очередной элемент>, <предыдущий элемент>)
# Для первого элемента предыдущим считается значение None.

# def with_previous(iterable):
#     yield from ((el, None) if i == -1 else (el, iterable[i]) for i, el in enumerate(iterable, -1))

# def with_previous(iterable):
#     prev = None
#     return ((i, prev, prev := i)[:-1] for i in iterable)




##############################################
# Реализуйте генераторную функцию, которая принимает один аргумент:
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:
# (<очередной элемент>, <следующий элемент>)
# Для последнего элемента следующим считается значение None.

# def pairwise(iterable):
#     if not iterable:
#         return []
#     iterable = iter(iterable)
#     first = next(iterable)
#     second = None
#     while first is not None:
#         yield (first, second := next(iterable, None))
#         first, second = second, first


##############################################


# Реализуйте генераторную функцию, которая принимает один аргумент:
#
# iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность
# кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы

def around(iterable):
    i = iter(iterable)
    e1, e2, e3 = None, next(i, None), next(i, None)
    while e2 is not None:
        yield e1, e2, e3
        e1, e2, e3 = e2, e3, next(i, None)


numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

