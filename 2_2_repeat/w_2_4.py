n = list(map(int, input().split()))
print(*(n[-1:] + n[:-1]))
