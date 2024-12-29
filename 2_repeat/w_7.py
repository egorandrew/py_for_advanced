n = str(input())[::-1]
my_str = ''
for i in range(len(n)):
    my_str += n[i]
    if (not (i + 1) % 3) and (i != 0) and i != len(n) - 1:
        my_str += ','
print(my_str[::-1])
