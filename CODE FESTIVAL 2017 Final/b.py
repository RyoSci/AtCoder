s = input()
abc = dict()
for i in "abc":
    abc[i] = 0

for i in s:
    abc[i] += 1

if max(abc.values()) - min(abc.values()) <= 1:
    print("YES")
else:
    print("NO")
