n, p = map(int, input().split())
divisors = dict()
div = 2
while p != 1:
    if p % div == 0:
        p //= div
        if div not in divisors:
            divisors[div] = 1
        else:
            divisors[div] += 1
    else:
        div += 1
    if div > 10 ** 6:
        divisors[p] = 1
        break

ans = 1
for div, div_num in divisors.items():
    ans = ans * div ** (div_num // n)

print(ans)
