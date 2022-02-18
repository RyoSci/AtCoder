n, k = map(int, input().split())
s = list(input())

if n == 1:
    print(0)
    exit()

cnt = 0
i = 0
while i < n-1:
    j = i+1
    if s[i] != s[j]:
        while j < n:
            if s[i] == s[j]:
                for l in range(i+1, j):
                    s[l] = s[i]
                i = j
                cnt += 1
                break
            else:
                j += 1
        else:
            for l in range(i+1, n):
                s[l] = s[i]
            break
        if cnt == k:
            break
    else:
        i += 1

res = 0
for i in range(1, n):
    if s[i] == s[i-1]:
        res += 1

print(res)
