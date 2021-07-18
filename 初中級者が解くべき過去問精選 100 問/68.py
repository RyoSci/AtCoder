n = int(input())
n_ = n

d = []
for i in range(2, int(n**0.5)+1):
    while 1:
        if n % i == 0:
            n //= i
            d.append(i)
        else:
            break

if n != 1:
    d.append(n)

print("%s: " % n_+" ".join(map(str, d)))
