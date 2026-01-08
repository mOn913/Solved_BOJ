n, m = map(int, input().split())
matrix_a = []
matrix_b = []
matrix_sum = [[0] * m for _ in range(n)]
for i in range(n):
    matrix_a.append(list(map(int, input().split())))

for i in range(n):
    matrix_b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in matrix_sum:
    print(' '.join(map(str, i)))