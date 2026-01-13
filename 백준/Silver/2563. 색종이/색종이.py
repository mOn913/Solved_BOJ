paper_num = int(input())
space = [[False for _ in range(100)] for _ in range(100)]
for i in range(paper_num):
    x, y = map(int, input().split())
    for n in range(x, x+10):
        for m in range(y, y+10):
            space[n][m] = True

extent = 0
for i in range(100):
    for j in range(100):
        if space[i][j]:
            extent += 1
print(extent)