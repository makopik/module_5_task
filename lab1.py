from collections import deque
import sys

def f(x, y):
    global OCT_NUM
    global result
    global transfer
    global sign
    OCT_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', }

    result = deque()
    transfer = 0
    sign = ''

    if len(y) > len(x):
        x, y = deque(y), deque(x)   
        sign='-'

    sum_x = 0
    sum_y = 0

    for item in x:
        sum_x -= OCT_NUM[item]

    for item in y:
        sum_y -= OCT_NUM[item]


    while x:

        if y:
            res = OCT_NUM[x.pop()] - OCT_NUM[y.pop()] - transfer

        else:
            res = OCT_NUM[x.pop()] - transfer

        if res < 0:
            result.appendleft(OCT_NUM[res % 8])
            transfer = 1
        else:
            result.appendleft(OCT_NUM[res])
            transfer = 0

    if sign == '-':
        result.appendleft(sign)

    return list(result)
a = list(input('Введите 1-е восьмиричное число: ').upper())
b = list(input('Введите 2-е восьмиричное число: ').upper())
print(a, b)
print(*a, '-', *b, '=', f(a.copy(), b.copy()))


#from Lab6 import show_size
#loc = locals().copy()
#show_size(loc)

def show_size(x, level=0):
    print('\t' * level,  f' type= {x.__class__}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__inter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
show_size(OCT_NUM)
show_size(result)
show_size(transfer)
show_size(sign)
show_size(f)


