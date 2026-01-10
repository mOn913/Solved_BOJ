matrix = []
max_len = 0
result = ""
for i in range(5):
    arr = list(input())
    matrix.append(arr)
    # 반복해야 하는 최소 횟수를 알기 위해 가장 긴 문자의 길이를 저장
    if len(arr) > max_len:
        max_len = len(arr)

for i in range(max_len):
    for j in range(5):
        # 길이가 가장 긴 행인 max_len만큼 반복하지만
        # 각 행의 길이보다 작을 때만 유효하도록 함
        if i < len(matrix[j]):
            result += matrix[j][i]
        
print(result)