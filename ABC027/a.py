l = list(map(int, input().split()))
l_s = list(set(l))
if len(l_s) == 1:
    print(l_s[0])
else:
    print((l_s[0] + l_s[1]) * 2 - sum(l))
