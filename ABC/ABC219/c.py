import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = input().strip()
x_order = [0]*26
for i in range(26):
    x_order[ord(x[i])-ord("a")] = i

n = int(input())
s = [input().strip() for _ in range(n)]

s2 = [[] for _ in range(n)]

for i in range(n):
    tmp = ""
    for j in s[i]:
        tmp += chr(x_order[ord(j)-ord("a")] + ord("a"))
    s2[i] = [tmp, s[i]]

s2.sort()

for i in range(n):
    print(s2[i][1])
