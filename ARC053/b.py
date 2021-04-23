s = input()
a2z = {}

for si in s:
    if si not in a2z:
        a2z[si] = 1
    else:
        a2z[si] += 1

odd = 0
even = 0
for val in a2z.values():
    odd += val % 2
    even += val // 2

if odd == 0:
    ans = even * 2
else:
    ans = even // odd * 2 + 1

print(ans)
