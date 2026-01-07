n = 100
while n > 0:
    try:
        print(input())
    except EOFError:
        break