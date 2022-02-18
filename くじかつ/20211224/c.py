import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
t = input().strip()

if n == 1 and t == "1":
    print(10**10*2)
else:
    s = ((n+2)//3+1)*"110"
    m = len(s)
    for i in range(m-n+1):
        if s[i:i+n] == t:
            tail = i+n-1+1
            break
    else:
        print(0)
        exit()
    token = (tail+2)//3

    print(10**10-token+1)
