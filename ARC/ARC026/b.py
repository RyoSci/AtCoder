n = int(input())
res = -n
for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0 and i != n:
        res += i
        if n // i != i:
            res += n // i
        
if res == n:
    ans = "Perfect"
elif res < n:
    ans = "Deficient"
else:
    ans = "Abundant"

print(ans)
