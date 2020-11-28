s = input()
abc = dict()
for i in "abc":
    abc[i] = 0

for i in s:
    abc[i] += 1

res = "01"
ans = "YES"
for i in range(len(s)):
    max_val = max(abc.values())
    max_abc = []
    for key, val in abc.items():
        if val == max_val:
            max_abc.append(key)
    for j in max_abc:
        if res[- 1] != j and res[- 2] != j and abc[j] != 0:
            abc[j] -= 1
            res += j
            break
    else:
        ans = "NO"

print(ans)
