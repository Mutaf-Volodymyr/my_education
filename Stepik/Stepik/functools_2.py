# Вам доступна уже реализованная функция send_email(), которая принимает три аргумента в следующем порядке:
#
# name — имя
# email_address — адрес электронной почты
# text — содержание письма
# Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.
#
# 1. Реализуйте функцию to_Timur() с помощью функции partial(), которая принимает один аргумент:
#
# text — содержание письма
# Функция должна отправлять письмо пользователю с именем Тимур на адрес timyrik20@beegeek.ru с содержанием text.
#
# 2. Реализуйте функцию send_an_invitation() с помощью функции partial(), которая принимает два аргумента в следующем порядке:
#
# name — имя
# email_address — адрес электронной почты
# Функция должна отправлять письмо на имя name и на адрес email_address со следующим содержанием:
#
# Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....


# from functools import partial
# to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
# send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')



######################## lru_cache
# from functools import lru_cache
# from sys import stdin
#
# @lru_cache()
# def aaaaaaaaaa(word):
#     res = ''.join(sorted(list(word)))
#     return res
#
# for line in stdin:
#     print(aaaaaaaaaa(line.strip()))




