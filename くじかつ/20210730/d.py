n = int(input())
a = list(map(int, input().split()))
s = [0]*(10**5+1)

for i in range(n):
    s[a[i]] += 1

res = 0
for i in range(10**5+1):
    res += max(0, s[i]-1)

print(n-(res+1)//2*2)
