a = int(input())
b = int(input())
ones = b % 10
tens = (b // 10) % 10
hundreds = b // 100

print(a * ones)
print(a * tens)
print(a * hundreds)
print(a * b)