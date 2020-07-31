
n, m = map(int, input().split())

swich = [0] * n

for i in range(m):
    _, *s = map(int, input().split())
    for j in range(len(s)):
        # swich[s[j] - 1] += 1 << (i)
        # swich[s[j] - 1] ^= 1 << (i)
        swich[s[j] - 1] |= 1 << (i)
    


p_list = list(map(int, input().split()))
p = 0
for i in range(m):
    # if p_list[i] == 1: 
    #     p += 1 << i
    p |= p_list[i] << i #上の処理と同じ

# print("++++++++++++++++++++++++")
# print(swich)
ans = 0
for i in range(1 << n):
    state_on_off = 0
    for index in range(n):
        if i >> index & 1 == 1:
            state_on_off ^= swich[index]
    if state_on_off == p:
        ans += 1
    # print(p, state_on_off,bin(i))
print(ans)