# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)

if n != 8:
    print("No")
    exit()

ans = "Yes"
if s[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ans = "No"

try:
    tmp = int(s[1:7])
    if not (10**5 <= tmp < 10**6):
        ans = "No"
except:
    ans = "No"

if s[-1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ans = "No"

print(ans)
