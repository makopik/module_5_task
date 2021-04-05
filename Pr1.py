from collections import deque

def f(x, y):
    OCT_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',}
    res = deque()
    t = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)


    while x:

        if y:
            res = OCT_NUM[x.pop()] - OCT_NUM[y.pop()] - t

        else:
            res = OCT_NUM[x.pop()] - t

        t = 0

        if res < 8:
            res.appendleft(OCT_NUM[res])

        else:
            res.appendleft(OCT_NUM[res - 8])
            t = 1

    if t:
        res.appendleft('1')

    return list(res)

a = list (input('Введите 1-е восьмиричное число: ').upper())
b = list (input('Введите 2-е восьмиричное число: ').upper())
print(a, b)

print(*a, '-', *b, '=', f(a, b))

