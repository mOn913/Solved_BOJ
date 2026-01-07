unit = list(map(int, input().split()))
total_unit = [1, 1, 2, 2, 2, 8]
require_unit = [0] * 6
for i in range(6):
    require_unit[i] = total_unit[i] - unit[i]
print(' '.join(str(x) for x in require_unit))