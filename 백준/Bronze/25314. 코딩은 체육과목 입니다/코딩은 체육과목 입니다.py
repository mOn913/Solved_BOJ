n = int(input())
type_str = "int"
for i in range(n // 4):
    type_str = "long " + type_str

print(type_str)