// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using namespace atcoder;
using lli = long long;
using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

ll pow_f(ll x, ll y) {
    ll rest = 1;
    while (y > 1) {
        if (y % 2 != 0) {
            rest *= x;
            rest %= MOD;
        }
        x = x * x;
        x %= MOD;
        y /= 2;
    }
    return x * rest % MOD;
}

ll f(ll n, ll k) {
    ll ans = 1;
    rep_r(i, n, n - k) {
        ans *= i;
        ans %= MOD;
    }
    rep_r(i, k, 0) {
        ans *= pow_f(i, MOD - 2);
        ans %= MOD;
    }
    return ans;
}

int main() {
    ll x, y;
    cin >> x >> y;
    ll n = 1e6 + 10;
    ll xx, yy;
    bool flag = false;
    ll a, b;
    rep(i, n) {
        xx = x - i * 1;
        yy = y - i * 2;
        if (xx == 2 * yy) {
            flag = true;
            a = i;
            b = xx / 2;
        }
    }
    if (flag) {
        cout << f(a + b, a) << "\n";
    } else
        cout << 0 << "\n";

    return 0;
}