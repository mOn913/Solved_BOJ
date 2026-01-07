n = int(input())
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")

    for k in range(0, (2*i)-1):
        print("*", end="")
    print()

for m in range(1, n):
    for p in range(m):
        print(" ", end="")

    for q in range((2*(n-m))-1, 0, -1):
        print("*", end="")
    print()
