#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define MOD 998244353
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
#include <atcoder/modint>
using namespace atcoder;
using mint = modint998244353;

Int find(vector<Int> &p, Int x) {
    if (p[x] < 0) return x;
    return p[x] = find(p, p[x]);
}

void unite(vector<Int> &p, Int x, Int y) {
    Int px = find(p, x);
    Int py = find(p, y);
    if (px == py) return;
    p[px] += p[py];
    p[py] = px;
    return;
}

Int pow_f(Int x, Int n) {
    // Int MOD = 998244353;
    Int ret = 1;
    while (n > 0) {
        if (n & 1)
            ret = ret * x % MOD;  // n の最下位bitが 1 ならば x^(2^i) をかける
        x = x * x % MOD;
        n /= 2;  // n を1bit 左にずらす
    }
    return ret;
}

int main() {
    Int n;
    cin >> n;
    vector<Int> f(n);
    for (Int i = 0; i < n; i++) cin >> f[i];

    vector<Int> par(n, -1);
    Int ans = 0;
    rep(i, n) {
        if (find(par, i) == find(par, f[i] - 1))
            ans++;
        else
            unite(par, i, f[i] - 1);
    }
    // cout << ans << "\n";
    // ans = pow(2, ans) - 1;
    // ans += MOD;
    // ans %= MOD;
    // cout << ans << "\n";
    // mint cnt = ans;
    cout << mint(2).pow(ans) - 1 << "\n";
    // cout << pow_f(2, ans) - 1 << "\n";
    return 0;
}