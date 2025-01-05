n = int(input())
k = int(input())
my_list = list(range(1, n + 1))
while len(my_list) > 1:
    for i in range(1, k):
        my_list = my_list[1:] + my_list[:1]
        if i == len(my_list):
            i = 0
    my_list.pop(0)
print(*my_list)
