# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
def input(): return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    ans = []
    n = int(input())
    s = input()
    i = n-1
    while i > -1:
        if s[i] == "0":
            ans.append(chr(int(s[i-2:i])-1+ord("a")))
            i -= 3
        else:
            ans.append(chr(int(s[i])-1+ord("a")))
            i -= 1
    ans = ans[::-1]
    print("".join(ans))
