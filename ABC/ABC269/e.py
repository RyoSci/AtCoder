# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

INF = 10**18

n = int(input())
lx, ly = 1, 1
rx, ry = n, n
while lx < rx:
    mx = (lx+rx)//2
    print("?", lx, mx, ly, ry, flush=True)
    t = int(input())
    if t == mx-lx+1:
        lx = mx+1
    else:
        rx = mx

ansx = lx
lx, ly = 1, 1
rx, ry = n, n
while ly < ry:
    my = (ly+ry)//2
    print("?", lx, rx, ly, my, flush=True)
    t = int(input())
    if t == my-ly+1:
        ly = my+1
    else:
        ry = my

ansy = ly
print("!", ansx, ansy, flush=True)
