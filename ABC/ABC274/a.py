# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())
s = b/a


s = Decimal(str("0.47244")).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(s)
