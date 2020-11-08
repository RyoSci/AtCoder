import itertools
n = int(input())
s = input()

ans = "None"
for i in itertools.permutations(s):
    i = "".join(i)
    if i == s:
        continue
    elif i == s[::-1]:
        continue
    else:
        ans = i
        break

print(ans)
