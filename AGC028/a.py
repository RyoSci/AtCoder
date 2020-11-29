n, m = map(int, input().split())
s = input()
t = input()


def gcd(a, b):
    while True:
        # div = a // b
        mod = a % b
        if mod == 0:
            return b
        a = b
        b = mod


lcm = m * n // gcd(m, n)
n_proceed = lcm // n
m_proceed = lcm // m
proceed_lcm = n_proceed * m_proceed // gcd(n_proceed, m_proceed)

ans = lcm
i = 1
while i <= lcm:
    si = (i - 1) * n // lcm
    ti = (i - 1) * m // lcm
    if s[si] != t[ti]:
        ans = -1
        break
    i += proceed_lcm

print(ans)
