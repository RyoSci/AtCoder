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
#define INF (1L << 62)
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
    ll n, k;
    cin >> n >> k;
    vector<ll> x(n), y(n);
    for (ll i = 0; i < n; i++) cin >> x[i] >> y[i];

    vector<P> xy;
    rep(i, n) { xy.emplace_back(make_pair(x[i], y[i])); }
    sort(xy.begin(), xy.end());
    sort(y.begin(), y.end());
    sort(x.begin(), x.end());

    vector<vector<ll>> grid(n + 1, vector<ll>(n + 1, 0));
    rep(i, n) {
        auto [xi, yi] = xy[i];
        ll dis = upper_bound(y.begin(), y.end(), yi) - y.begin();
        grid[i + 1][dis] = 1;
    }

    rep(i, n) rep(j, n) {
        grid[i + 1][j + 1] += grid[i][j + 1] + grid[i + 1][j] - grid[i][j];
    }

    ll ans = INF;
    rep_s(l, 1, n) rep_s(r, l + 1, n + 1) rep_s(d, 1, n)
        rep_s(u, d + 1, n + 1) {
        ll cnt =
            grid[u][r] - grid[u][l - 1] - grid[d - 1][r] + grid[d - 1][l - 1];
        ll area = (x[u - 1] - x[d - 1]) * (y[r - 1] - y[l - 1]);
        if (cnt >= k) ans = min(ans, area);
    }

    cout << ans << "\n";
    return 0;
}