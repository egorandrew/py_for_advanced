n = int(input())
my_set = []
word = "anton"

for i in range(1, n + 1):
    my_str = input()
    m = 0
    for buk in my_str:
        if buk == word[m]:
            m += 1
            if m == len(word):
                my_set.append(i)
                break
print(*my_set)

