s = input()
k = int(input())
n = len(s)
mark = [0]*(2*n)
s2 = s+s
i = 0
while i < 2*n-1:
    if s2[i] == s2[i+1]:
        mark[i+1] = 1
        i += 2
    else:
        i += 1

if len(set(s)) == 1:
    res = sum(mark[n:])*(k//2)+sum(mark[:n])*((k+1)//2)
else:
    res = sum(mark[n:])*(k-1)+sum(mark[:n])
print(res)
