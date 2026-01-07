time = 2
total_time = 0
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
w = input()
for i in w:
    for j in range(8):
        if i in dial[j]:
            total_time += (j+1) + time
print(total_time)