n = int(input())
is_plus = n >= 0
n = abs(n)

n_bin = []
while n > 0:
    n_bin.append(n % 2)
    n //= 2

n_bin.append(0)
n_bin.append(0)

for i in range(len(n_bin)-1):
    if is_plus and i % 2 == 1:
        n_bin[i] = -n_bin[i]
    elif not is_plus and i % 2 == 0:
        n_bin[i] = -n_bin[i]

for i in range(len(n_bin) - 1):
    if n_bin[i] == -1:
        n_bin[i] += 2
        n_bin[i+1] += 1
    elif n_bin[i] == 2:
        n_bin[i] = 0
        n_bin[i+1] -= 1
    elif n_bin[i] == -2:
        n_bin[i] = 0
        n_bin[i+1] += 1

n_bin = n_bin[::-1]
for i in range(len(n_bin)):
    if n_bin[i] == 1:
        break

print(*n_bin[i:], sep="")

#     n_bin = n_bin[::-1]
#     ans = 0
#     for i in range(len(n_bin)):
#         if i % 2 == 0:
#             ans += (2**i)*n_bin[i]
#         else:
#             ans -= (2**i)*n_bin[i]
#     if ans == n_ and (ans >= 0) == is_plus:
#         continue
#     else:
#         print("NO", n_, ans)
#         break
# else:
#     print("OK")
