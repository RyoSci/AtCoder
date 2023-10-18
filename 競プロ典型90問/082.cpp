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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

mint g(ll s, ll e) {
    mint cnt = e - s + 1;
    cnt *= s + e;
    cnt /= 2;
    return cnt;
}
mint f(ll x) {
    mint res = 0;
    rep(i, 19) {
        ll l = powl(10, i);
        if (i == 18 and l <= x) {
            ll r = x;
            res += (i + 1) * g(l, r);
        } else if (l <= x) {
            ll r = min(x, powl(10, i + 1) - 1);
            res += (i + 1) * g(l, r);
        }
    }
    return res;
}

int main() {
    ll l, r;
    cin >> l >> r;

    mint ans = f(r) - f(l - 1);
    cout << ans.val() << "\n";

    return 0;
}