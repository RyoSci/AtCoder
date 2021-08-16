n = int(input())
n *= 2

res = 0
for x in range(1, int(n**0.5)+1):
    if n % x == 0:
        y = n//x
        a = x+y-1
        b = x-y+1
        if a % 2 == 0 and b % 2 == 0:
            res += 1

print(res*2)
