n, c = map(int, input().split())
even = [[0, i] for i in range(10)]
odd = [[0, i] for i in range(10)]

for i in range(n):
    ai = int(input())
    if i % 2 == 0:
        even[ai - 1][0] += 1
    else:
        odd[ai - 1][0] += 1

even.sort(key=lambda x: x[0], reverse=True)
odd.sort(key=lambda x: x[0], reverse=True)

if even[0][1] == odd[0][1]:
    e_sec = 0
    o_sec = 0
    if len(even) > 1:
        e_sec = even[1][0]
    if len(odd) > 1:
        o_sec = odd[1][0]
    res = min((n + 1) // 2 - even[0][0] + n // 2 - o_sec, (n + 1) // 2 - e_sec + n // 2 - odd[0][0])
else:
    res = (n + 1) // 2 - even[0][0] + n // 2 - odd[0][0]

res *= c
print(res)
