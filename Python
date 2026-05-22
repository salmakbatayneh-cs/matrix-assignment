def add(a, b):
    r = []

    for i in range(len(a)):
        row = []

        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])

        r.append(row)

    return r


def mul(a, b):
    r = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                r[i][j] += a[i][k] * b[k][j]

    return r


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv(a):
    d = det(a)

    if d == 0:
        return "no inverse"

    return [
        [a[1][1] / d, -a[0][1] / d],
        [-a[1][0] / d, a[0][0] / d]
    ]


def solve(a, b):
    x = inv(a)

    return mul(x, b)


a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]

c = [
    [5],
    [6]
]

print(add(a, b))
print(mul(a, b))
print(det(a))
print(inv(a))
print(solve(a, c))
