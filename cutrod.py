def lcs_length(x, y, m, n):
    b = [[0] * (n + 1) for i in range(m + 1)]
    c = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "q"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "i"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "-"
    return (b, c)

def print_lcs(b, x, i, j):
    if i == 0:
        return
    if b[i][j] == "q":
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end="")
    elif b[i][j] == "i":
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)

X = ['D', 'F', 'A', 'D', 'B', 'D', 'C', 'E', 'B', 'E', 'A', 'G']
Y = ['E', 'F', 'B', 'E', 'G', 'E', 'C', 'A', 'E', 'B', 'D', 'A']
m = 12
n = 12
b, c = lcs_length(X, Y, m, n)
print_lcs(b, X, 11, 11)
for row in b:
    print(row)
for row in c:
    print(row)

    