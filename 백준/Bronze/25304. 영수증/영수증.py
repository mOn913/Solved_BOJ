total = int(input())
type_num = int(input())
sum = 0

for i in range(type_num):
    price, count = map(int, input().split())
    for j in range(count):
       sum += price
    
print("Yes" if total == sum else "No")