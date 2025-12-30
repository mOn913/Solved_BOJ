hour, min = map(int, input().split())
cooking_time = int(input())

add_hour = cooking_time // 60
add_min = cooking_time % 60

min += add_min
hour += add_hour
if min >= 60:
    min -= 60
    hour += 1
if hour > 23:
    hour -= 24

print(hour, min)