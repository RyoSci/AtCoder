n = int(input())
s = sorted(list(map(int, input().split())))
q = int(input())
t = list(map(int, input().split()))


def binary_search(s, ti):
    l = 0
    r = len(s)-1
    m = (l+r)//2
    while l+1 < r:
        if s[m] == ti:
            break
        elif s[m] < ti:
            l = m
        else:
            r = m
        m = (l+r)//2
    if s[m] == ti or s[l] == ti or s[r] == ti:
        return True
    else:
        return False


res = 0
for ti in t:
    res += binary_search(s, ti)

print(res)
