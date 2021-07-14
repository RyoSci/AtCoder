n = int(input())
p = [int(input()) for _ in range(n)]
p.sort()
res = sum(p[:n-1])+p[-1]//2
print(res)
