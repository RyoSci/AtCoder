n = int(input())
s = input()
t = input()

ans = 2*n
for i in range(n):
    for j in range(n-i):
        if s[i+j] != t[j]:
            break
    else:
        ans = n+i
        break
print(ans)
