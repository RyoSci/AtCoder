s = input()
n = int(input())
for i in range(n):
    l, r = map(lambda x: int(x) - 1, input().split())
    tmp = s[l:r + 1][::-1]
    s = s[:l] + tmp + s[r + 1:]

print(s)
