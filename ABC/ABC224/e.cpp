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
#define INF (1LL << 60)
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
    ll h, w, n;
    cin >> h >> w >> n;
    vector<ll> r(n), c(n), a(n);
    rep(i, n) cin >> r[i] >> c[i] >> a[i];

    map<ll, vector<ll>> a2i;
    set<ll> tmp;
    rep(i, n) {
        a2i[a[i]].emplace_back(i);
        tmp.insert(a[i]);
    }

    vector<ll> reva;
    rep_e(e, tmp) reva.emplace_back(e);
    reverse(reva.begin(), reva.end());

    vector<ll> cols(h + 1, 0);
    vector<ll> rows(w + 1, 0);

    vector<ll> ans(n);

    rep_e(ai, reva) {
        rep_e(i, a2i[ai]) {
            ll ri = r[i];
            ll ci = c[i];

            ll now = 1;
            // 横方向
            now = max(now, cols[ri] + 1);

            // 縦方向
            now = max(now, rows[ci] + 1);

            ans[i] = now;
        }

        rep_e(i, a2i[ai]) {
            ll ri = r[i];
            ll ci = c[i];

            ll now = ans[i];

            cols[ri] = max(cols[ri], now);
            rows[ci] = max(rows[ci], now);
        }
    }

    rep(i, n) { cout << ans[i] - 1 << "\n"; }

    return 0;
}