n_m_l = list(map(int, input().split()))
p_q_r = list(map(int, input().split()))


ans = 0
for i in range(3):
    tmp = n_m_l[::]
    l = tmp.pop(i)
    n, m = tmp
    for j in range(3):
        bug = p_q_r[::]
        r = bug.pop(j)
        for k in range(2):
            p, q = bug
            if k:
                p, q = q, p
            ans = max(ans, (n // p) * (m // q) * (l // r))

print(ans)
