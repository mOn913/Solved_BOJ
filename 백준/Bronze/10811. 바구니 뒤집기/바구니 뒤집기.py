n, m = map(int, input().split())

basket = [x for x in range(1, n+1)]
for i in range(m):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(' '.join(str(x) for x in basket))