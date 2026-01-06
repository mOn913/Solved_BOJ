import sys
remain = []
for i in range(10):
    num = int(sys.stdin.readline())
    remain.append(num % 42)

print(len(set(remain)))