n = int(input())
first_, second_, third_, fourth_ = 0, 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    first_ += x > 0 and y > 0
    second_ += x < 0 < y
    third_ += x < 0 and y < 0
    fourth_ += y < 0 < x
print(f"Первая четверть: {first_}\nВторая четверть: {second_}\nТретья четверть: {third_}\nЧетвертая четверть: {fourth_}")
