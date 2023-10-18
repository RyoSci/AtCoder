import random
"https://tjkendev.github.io/procon-library/python/string/rolling_hash.html"
"https://kyoroid.github.io/algorithm/string/rolling_hash.html"

# 1-dimension Rolling Hash


class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        """S[l, r) のハッシュを求める"""
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

    def connect(self, h1, h2, h2len):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        return (h1*self.pw[h2len] + h2) % self.mod

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        # LCPの最小値 (範囲内)
        low = 0
        # LCPの最大値 + 1 (範囲外)
        high = min(r1-l1, r2-l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low


base = 37
mod0 = 1000000007
mod1 = 100000000000031

# 衝突が怖いなら数回判定する
"https://snuke.hatenablog.com/entry/2017/02/03/035524"


####################################################################################
# classにあらかじめmod, baseを入れておく

"https://tjkendev.github.io/procon-library/python/string/rolling_hash.html"
"https://kyoroid.github.io/algorithm/string/rolling_hash.html"

# 1-dimension Rolling Hash


class RollingHash():
    def __init__(self, s):

        # 衝突が怖いなら数回判定する
        "https://snuke.hatenablog.com/entry/2017/02/03/035524"
        self.mod0 = 1000000007
        self.mod1 = 100000000000031
        self.pw0 = [1]*(len(s)+1)
        self.pw1 = [1]*(len(s)+1)
        # self.base = 37
        self.base = random.randint(0, self.mod0 - 1)

        l = len(s)
        self.h0 = [0]*(l+1)
        self.h1 = [0]*(l+1)

        v0 = 0
        v1 = 0
        for i in range(l):
            self.h0[i+1] = v0 = (v0 * self.base + ord(s[i])) % self.mod0
            self.h1[i+1] = v1 = (v1 * self.base + ord(s[i])) % self.mod1
        v0 = 1
        v1 = 1
        for i in range(l):
            self.pw0[i+1] = v0 = v0 * self.base % self.mod0
            self.pw1[i+1] = v1 = v1 * self.base % self.mod1

    def get(self, l, r):
        """S[l, r) のハッシュを求める"""
        res0 = (self.h0[r] - self.h0[l] * self.pw0[r-l]) % self.mod0
        # return res0
        res1 = (self.h1[r] - self.h1[l] * self.pw1[r-l]) % self.mod1
        return (res0, res1)

    def connect(self, h1, h2, h2len):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        res0 = (h1*self.pw0[h2len] + h2) % self.mod0
        # return res0
        res1 = (h1*self.pw1[h2len] + h2) % self.mod1
        return (res0, res1)

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        # LCPの最小値 (範囲内)
        low = 0
        # LCPの最大値 + 1 (範囲外)
        high = min(r1-l1, r2-l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low
