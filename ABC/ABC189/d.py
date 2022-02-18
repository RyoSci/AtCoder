n = int(input())
s = [input() for _ in range(n)]


def cal(s, is_ture):
    if len(s) == 0:
        return 1
    if is_ture == (s[-1] == "AND"):
        tmp = cal(s[:-1], is_ture)
    else:
        tmp = 2**(len(s)+1)-cal(s[:-1], is_ture ^ True)
    return tmp


res = cal(s, True)
print(res)
