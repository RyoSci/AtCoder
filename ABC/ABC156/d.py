n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
double_check = set()
num = 2
for i in range(10 ** 6 + 1):
    if num not in double_check:
        double_check.add(num)
    else:
        break
    num = (num * 2) % mod

for i in range(10 ** 3):
    num = num * 2 % mod

num_a = n
for i in range(1, a):
    num_a = (num_a * (n - i)) % mod

for i in range(1, a + 1):
    num_a = num_a // i

print(num_a % mod)
