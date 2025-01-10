n = list(map(int, input().split()))
my_list = []
for i in range(len(n) - 1):
    if n[i] < n[i+1]:
        my_list.append(n[i+1])
print(len(my_list))
