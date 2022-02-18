# # from collections import defaultdict
# # import re
# # import sys
# # sys.setrecursionlimit(10**6)
# # input = sys.stdin.readline

# # # n = int(input())
# # # a = list(map(int, input().split()))


# # # def quick_sort(a):
# # #     if len(a) == 0:
# # #         return a
# # #     l = []
# # #     r = []

# # #     n = len(a)
# # #     x = n//2

# # #     for i in range(n):
# # #         if i == x:
# # #             continue
# # #         if a[i] < a[x]:
# # #             l.append(a[i])
# # #         else:
# # #             r.append(a[i])

# # #     l = quick_sort(l)
# # #     r = quick_sort(r)

# # #     a = l+[a[x]]+r
# # #     return a


# # # a = quick_sort(a)

# # # print(*a)


# # n = int(input())
# # a = list(map(int, input().split()))


# # def merge_sort(a):
# #     n = len(a)
# #     if n <= 1:
# #         return a
# #     x = n//2
# #     l = []
# #     r = []
# #     for i in range(x):
# #         l.append(a[i])
# #     for i in range(x, n):
# #         r.append(a[i])
# #     l = merge_sort(l)
# #     r = merge_sort(r)
# #     l = l+r[::-1]
# #     b = []
# #     i = 0
# #     j = n-1

# #     while i <= j:
# #         if l[i] <= l[j]:
# #             b.append(l[i])
# #             i += 1
# #         else:
# #             b.append(l[j])
# #             j -= 1
# #     return b


# # a = merge_sort(a)


# # print(*a)


# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# "https://judge.yosupo.jp/submission/7795"


# class SegTree:
#     X_unit = 0
#     X_f = sum

#     def __init__(self, N):
#         self.N = N
#         self.X = [self.X_unit] * (N + N)

#     def build(self, seq):
#         for i, x in enumerate(seq, self.N):
#             self.X[i] = x
#         for i in range(self.N - 1, 0, -1):
#             self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

#     def set_val(self, i, x):
#         i += self.N
#         self.X[i] = x
#         while i > 1:
#             i >>= 1
#             self.X[i] = self.X_f([self.X[i << 1], self.X[i << 1 | 1]])
#             # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

#     def add_val(self, i, x):
#         i += self.N
#         self.X[i] += x
#         while i > 1:
#             i >>= 1
#             self.X[i] = self.X_f([self.X[i << 1], self.X[i << 1 | 1]])
#             # self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

#     def fold(self, L, R):
#         L += self.N
#         R += self.N
#         vL = self.X_unit
#         vR = self.X_unit
#         while L < R:
#             if L & 1:
#                 vL = self.X_f([vL, self.X[L]])
#                 # vL = self.X_f(vL, self.X[L])
#                 L += 1
#             if R & 1:
#                 R -= 1
#                 vR = self.X_f([self.X[R], vR])
#                 # vR = self.X_f(self.X[R], vR)
#             L >>= 1
#             R >>= 1
#         return self.X_f([vL, vR])
#         # return self.X_f(vL, vR)


# N, Q = map(int, readline().split())
# seg = SegTree(N)

# ans = []
# for i in range(Q):
#     c, x, y = map(int, input().split())
#     if c == 0:
#         seg.add_val(x-1, y)
#     else:
#         ans.append(seg.fold(x-1, y))

# print(*ans, sep="\n")


# from bisect import bisect_left
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# for i in range(m):
#     index = bisect_left(a, b[i])
#     print(index)

n = 100
for n in range(100, 200):

    def f(x, y):
        x = x+y
        flag = False
        for i in range(1, x+1):
            if i*i > x:
                break
            if i*i == x:
                flag = True
        return flag

    ans = []
    for a in range(n, 2*n+1-2):
        for b in range(a+1, 2*n+1-1):
            for c in range(b+1, 2*n+1):
                if f(a, b) and f(b, c) and f(c, a):
                    # print(n, a, b, c)
                    ans.append([n, a, b, c])
    print(*ans)
