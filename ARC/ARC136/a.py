from re import template


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
s = input().strip()

ans = []
now = s[0]
i = 1
while i < n:
    if now == 'C' or now == 'A':
        ans.append(now)
        now = s[i]
        i += 1
    else:
        if s[i] == 'A':
            ans.append('A')
            now = 'B'
            i += 1
        elif s[i] == 'B':
            ans.append('A')
            i += 1
            if i < n:
                now = s[i]
            else:
                now = ""
            i += 1
        else:
            ans.append('B')
            now = 'C'
            i += 1

ans.append(now)

print("".join(ans))
