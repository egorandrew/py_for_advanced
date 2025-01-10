n = list(map(int, input().split()))
my_list = []
for i in n:
    if i not in my_list:
        my_list.append(i)
print(len(my_list))
print(len(set(n)))
