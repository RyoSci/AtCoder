import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a,b,c,d = list(map(int, input().split()))

def is_prime(x):
    res=True
    for i in range(2,x):
        if i*i>x:
            break
        if x%i==0:
            res=False
    return res


ans="Aoki"
for t in range(a, b+1):
    for a in range(c, d+1):
        if is_prime(t+a):
            break
    else:
        ans="Takahashi"
        break

print(ans)