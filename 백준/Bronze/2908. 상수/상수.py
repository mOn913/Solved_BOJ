a, b = map(str, input().split())
r_a = a[::-1]
r_b = b[::-1]
print(r_a if r_a > r_b else r_b)