from random import randint

# 説明記事
"https://qiita.com/Shirotsume/items/890afc81988c63ae9603"

# ソース元記事
"https://codeforces.com/blog/entry/101817?mobile=true"

RANDOM = randint(1, 10 ** 9)


class Wrapper(int):
    """
    intを入れて使う
    """

    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


"""hack case"""

size = 2 ** 32
d = {}
d[size + 1] = 1
x = 6
for i in range(2 * 10 ** 5):
    wx = Wrapper(x)
    d[wx] = 1

    # d[x] = 1
    x = 5 * x + 1
    x %= size

for i in range(2 * 10 ** 5):
    w1 = Wrapper(1)
    d[w1] = 1

    # d[1] = 1

print("Done")

""""""
