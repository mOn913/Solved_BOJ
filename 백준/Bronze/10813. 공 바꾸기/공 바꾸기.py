n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]

for _i in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for num in basket:
    print(num, end=" ")