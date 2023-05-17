import sys


def to_2(num):
    str_repr = ''
    while num != 0:
        str_repr += str(num % 2)
        num = num // 2

    return str_repr[::-1]


def func(a, b):
    if b == 1:
        return a

    res = func(a, b - 1) ** a
    return res


line = sys.stdin.readline().strip().split()

f_num = 1
counter = 0
for i in to_2(func(int(line[0]), int(line[1])-1)):
    if i == '1':
        f_num *= int(line[0])**(2**counter) % int(line[2])
    counter += 1

print(f_num % int(line[2]))

