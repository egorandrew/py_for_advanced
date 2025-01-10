n = input().split()
# my_list = []
# i = 0
# j = 1
# for a in range(len(n) // 2):
#     my_list.append(n[j])
#     my_list.append(n[i])
#     i += 2
#     j += 2
# if len(n) % 2:
#     my_list.append(n[-1])

# j = 0
# if len(n) != 1:
#     for i in range(0, len(n)//2):
#         n.insert(j, n[j + 1])
#         n.pop(j + 2)
#         j += 2

for i in range(0, len(n) - 1, 2):
    n[i], n[i+1] = n[i+1], n[i]

print(*n)


