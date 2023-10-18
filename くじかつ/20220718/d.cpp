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

vector<ll> a(2 * 10e5 + 10, 0);

vector<ll> dp_min(2 * 10e5 + 10, -1);
// vector<ll> dp_max(2 * 10e5 + 10, -1);

vector<ll> seen(2 * 10e5 + 10, 0);

vector<vector<ll>> g(2 * 10e5 + 10);

ll ans = -INF;

void dfs(ll par, ll root = -1) {
    seen[par] = 1;
    rep_e(chi, g[par]) {
        // if (chi == root) continue;
        ans = max(ans, a[chi] - a[dp_min[par]]);
        if (seen[chi] == 1) continue;

        // if (a[dp_max[chi]] >= a[dp_max[par]])
        //     dp_max[chi] = chi;
        // else
        //     dp_max[chi] = dp_max[par];
        if (a[dp_min[chi]] <= a[dp_min[par]])
            dp_min[chi] = chi;
        else
            dp_min[chi] = dp_min[par];

        dfs(chi, par);
    }
}

int main() {
    ll n, m;
    cin >> n >> m;
    // vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> x(m), y(m);
    for (ll i = 0; i < m; i++) cin >> x[i] >> y[i];

    rep(i, m) { g[x[i] - 1].push_back(y[i] - 1); }
    rep(i, n) sort(g[i].begin(), g[i].end());

    rep(i, n) {
        dp_min[i] = i;
        // dp_max[i] = i;
    }

    rep(i, n) {
        if (seen[i]) continue;
        dfs(i);
    }

    cout << ans << "\n";
    return 0;
}