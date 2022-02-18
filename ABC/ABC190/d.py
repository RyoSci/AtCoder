n = int(input())

res = 0
for i in range(1, 10**7+1):
    s = i*(i+1)//2
    if n-s >= 0 and (n-s) % i == 0:
        res += 1

print(res*2)
