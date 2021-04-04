n = int(input())
a = list(map(int, input().split()))
digits = [0] * 60

for ai in a:
    for i in range(60):
        digits[i] += ai % 2
        ai //= 2
        if ai == 0:
            break
    
res = 0
mod = 10 ** 9 + 7
mul = 1
for i in range(60):
    res = (res + (n - digits[i]) * digits[i] * mul) % mod
    mul *= 2

print(res)