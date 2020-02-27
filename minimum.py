from sys import maxsize

def minimum(array):
    column = maxsize
    raw = maxsize
    ir = 0
    for i, r in enumerate(array):
        s = sum(r)
        if s < raw:
            raw = s
            ir = i
    ic = 0
    for i in range(len(array[0])):
        sum_column = 0
        for r in array:
            sum_column += r[i]
        if sum_column < column:
            column = sum_column
            ic = i

    return [ir, ic]

print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

