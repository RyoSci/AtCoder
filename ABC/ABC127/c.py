"""
TLE出るはず！！！
データが連続であるから、集合をとって和集合を取る必要はなかった！
"""
n, m = map(int, input().split())
line = set(range(1, n + 1))
for i in range(m):
    l, r = map(int, input().split())
    line &= set(range(l, r + 1))

print(len(line))
