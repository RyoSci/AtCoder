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

int main() {
    ll n, k, p;
    cin >> n >> k >> p;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b;
    ll l = n / 2;
    rep_s(i, l, n) b.emplace_back(a[i]);

    vector<vector<ll>> tot(n + 1);

    rep(i, 1 << l) {
        ll cnt = 0;
        ll res = 0;
        rep(j, l) {
            if (i >> j & 1) {
                cnt++;
                res += a[j];
            }
        }
        tot[cnt].emplace_back(res);
    }

    rep(i, n) sort(tot[i].begin(), tot[i].end());

    ll ans = 0;
    ll r = n - l;
    rep(i, 1 << r) {
        ll cnt = 0;
        ll res = 0;
        rep(j, r) {
            if (i >> j & 1) {
                cnt++;
                res += b[j];
            }
        }
        if (k - cnt >= 0) {
            auto iter =
                upper_bound(tot[k - cnt].begin(), tot[k - cnt].end(), p - res);
            ll dis = iter - tot[k - cnt].begin();
            ans += dis;
        }
    }
    cout << ans << "\n";

    return 0;
}