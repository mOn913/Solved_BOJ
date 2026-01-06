import sys
isAttend = [False] * 30
for i in range(28):
    num = int(sys.stdin.readline())
    isAttend[num-1] = True

notAttend = []

for i in range(30):
    if not isAttend[i]:
        notAttend.append(i+1)
notAttend.sort()
print(notAttend[0])
print(notAttend[1])