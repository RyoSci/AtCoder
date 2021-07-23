n = int(input())

res = 0
for a in range(1, int(n**0.5)+1):
    if n % a == 0:
        m_1 = n//a
        if m_1 > a+1:
            res += m_1-1

print(res)
