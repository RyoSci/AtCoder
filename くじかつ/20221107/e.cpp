// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
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

int main() {
    ll n, t;
    cin >> n >> t;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    vector<ll> b, c;
    rep(i, n) {
        if (i >= n / 2)
            c.emplace_back(a[i]);
        else
            b.emplace_back(a[i]);
    }

    vector<ll> csum;
    ll m = b.size();
    ll l = c.size();

    rep(i, 1 << l) {
        ll res = 0;
        rep(j, l) if ((i >> j) & 1) res += c[j];
        csum.emplace_back(res);
    }
    sort(csum.begin(), csum.end());

    ll ans = 0;
    rep(i, 1 << m) {
        ll res = 0;
        rep(j, m) if ((i >> j) & 1) res += b[j];
        auto pos =
            upper_bound(csum.begin(), csum.end(), t - res) - csum.begin();
        if (pos > 0) res += csum[pos - 1];
        if (res <= t) ans = max(ans, res);
    }

    cout << ans << "\n";
    return 0;
}