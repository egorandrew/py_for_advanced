n = int(input())
my_list = [int(input()) for i in range(n)]
number = int(input())
have = "НЕТ"
for i in enumerate(my_list):
    if have == "НЕТ":
        for j in enumerate(my_list[i[0] + 1:]):
            if i[1]*j[1] == number:
                have = "ДА"
                break
    else:
        break
print(have)
