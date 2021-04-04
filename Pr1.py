from collections import deque

def delen(x, y):
    Nom = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = Nom[x.pop()] / Nom[y.pop()] + transfer
        else:
            res = Nom[x.pop()] / transfer
        transfer = 0
        if res < 16:
            result.appendleft(Nom[res])
        else:
            result.appendleft(Nom[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)
a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(*a, '/', *b, '=', *delen(a, b))

