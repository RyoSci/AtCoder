n, k = map(int, input().split())
s = input()
zero_one = []
tmp = s[0]
for i in range(1, n):
    if tmp[-1] == s[i]:
        tmp += s[i]
    else:
        zero_one.append([tmp[-1], len(tmp)])
        tmp = s[i]

zero_one.append([tmp[-1], len(tmp)])

res = 0
cnt = 0
tmp = 0
j = 0
for i in range(len(zero_one)):
    if cnt == k and zero_one[i][0] == "0":
        cnt += 1
        tmp += zero_one[i][1]
        while True:
            if cnt <= k:
                break
            if zero_one[j][0] == "0":
                cnt -= 1
            tmp -= zero_one[j][1]
            j += 1
    else:
        if zero_one[i][0] == "0":
            cnt += 1
        tmp += zero_one[i][1]
    res = max(res, tmp)

print(res)
