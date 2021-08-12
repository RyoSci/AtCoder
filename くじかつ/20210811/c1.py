import sys

# s = input()
# print(sys.argv)
s = sys.argv[1]
d = [0]*8

chokudai = "chokudai"
mod = 10**9+7

for i in range(len(s)):
    for j in range(8):
        if s[i] == chokudai[j] and chokudai[j] == "c":
            d[0] += 1
            d[0] %= mod
        elif s[i] == chokudai[j]:
            d[j] += d[j-1]
            d[j] %= mod

print(d[-1])
