# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
import hashlib

def get_num_substrings(string: str):
    LENGTH = len(string)
    left = 0
    right = 1
    step = 1
    hash_list = set()
    while right != LENGTH:
        while right != LENGTH + 1:
            hash_list.add(hashlib.sha1(string[left:right].encode('utf-8')).hexdigest())
            left += 1
            right += 1
        step += 1
        left = 0
        right = step
    return len(hash_list)


user_string = input('Что-нибудь: ')
print(get_num_substrings(user_string))