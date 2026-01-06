n, m = map(int, input().split())
basket = [0] * n
for _i in range(m):
    i, j, k = map(int, input().split())
    for _j in range(i-1, j):
        basket[_j] = k

for num in basket:
    print(num)
