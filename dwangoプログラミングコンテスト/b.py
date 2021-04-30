s = input()
nico_cnt = dict()
n = len(s)

i = 0
while i < n - 1:
    if s[i:i + 2] == "25":
        j = i + 2
        cnt = 1
        while j < n - 1:
            if s[j:j + 2] == "25":
                cnt += 1
                i = j + 1
                j += 2
            else:
                break
        if cnt not in nico_cnt:
            nico_cnt[cnt] = 1
        else:
            nico_cnt[cnt] += 1
    i += 1

if len(nico_cnt) == 0:
    print(0)
else:
    # dp = [0] * (max(nico_cnt.keys()) + 1)
    # for i in range(max(nico_cnt.keys()) + 1):
    #     dp[i] = dp[i - 1] + i

    ans = 0
    for key, val in nico_cnt.items():
        # ans += dp[key] * val
        ans += key * (key + 1) // 2 * val

    print(ans)
