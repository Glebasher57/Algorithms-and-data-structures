# Закодируйте любую строку по алгоритму Хаффмана

import sys
from collections import Counter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def get_node(self):
        return self.left, self.right


def get_encode_table(node, code=''):
    if isinstance(node, str):
        return {node: code}
    left, right = node.get_node()
    result = {}
    result.update(get_encode_table(left, code + '0'))
    result.update(get_encode_table(right, code + '1'))
    return result


user_string = input('Введите строку: ')
tree = Counter(user_string)
tree = tree.items()

while len(tree) > 1:
    tree = sorted(tree, key=lambda x: x[1], reverse=True)
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree.pop()
    tree.pop()
    tree.append((MyNode(char1, char2), count1 + count2))

encode_table = get_encode_table(tree[0][0])

result = ''
for char in user_string:
    result += encode_table.get(char)

print(f'Строка "{user_string}" - закодирована (￣^￣)ゞ', result, sep='\n')
print(f'Спасибо за курс, было очень интересно и познавательно ＼(￣▽￣)／')