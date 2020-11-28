s = input()
abc = [0] * 3
abc = [[0, 0], [0, 1], [0, 2]]
for i in s:
    if i == "a":
        abc[0][0] += 1
    elif i == "b":
        abc[1][0] += 1
    else:
        abc[2][0] += 1

abc_sorted = sorted(abc)
max1 = abc_sorted[2][1]
max2 = abc_sorted[1][1]
max3 = abc_sorted[0][1]

abc = [i[0] for i in abc]

order = [max1, max2, max3]
for i in range(len(s)):
    order_i = i % 3
    abc[order[order_i]] -= 1
    if min(abc) == max(abc) == 0:
        ans = "YES"
        break
else:
    ans = "NO"

print(ans)
