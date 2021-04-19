from collections import deque


def f(x, y):
    OCT_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', }

    result = deque()
    transfer = 0
    sign = ''

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    sum_x = 0
    sum_y = 0

    for item in x:
        sum_x += OCT_NUM[item]

    for item in y:
        sum_y += OCT_NUM[item]


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
                if len(y) < len(x):
                    x, y = deque(y), deque(x)
                    sign = '-'
            result.appendleft(sign)

    return list(result)


a = list(input('Введите 1-е восьмиричное число: ').upper())
b = list(input('Введите 2-е восьмиричное число: ').upper())
print(a, b)

print(*a, '-', *b, '=', f(a, b))