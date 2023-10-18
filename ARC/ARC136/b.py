from itertools import permutations
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# a = [1, 2, 3, 4]
# ans = set()


# def dfs(a):
#     if tuple(a) in ans:
#         return
#     ans.add(tuple(a))
#     w, x, y, z = a
#     dfs([x, y, w, z])
#     dfs([w, y, z, x])


# dfs(a)
# ans = list(ans)
# ans.sort()
# print(*ans, sep="\n")
# print("##")
# print(*list(permutations(range(1, 5))), sep="\n")


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
for i in range(n):
    t = a[i]
    for j in range(i+1, n):
        if a[i] == b[j]:
            if i != j:
                b[i:] = b[j:j+1]+b[:j]+b[j+1:]
                cnt += (j-i)
                break
    else:
        print("No")
        exit()


print("Yes" if cnt % 2 == 0 else "No")
