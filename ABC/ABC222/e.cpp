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
    ll n, m, k;
    cin >> n >> m >> k;
    vector<ll> a(m);
    for (ll i = 0; i < m; i++) {
        cin >> a[i];
        a[i]--;
    }

    vector<vector<ll>> g(n);
    rep(i, n - 1) {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].emplace_back(v);
        g[v].emplace_back(u);
    }

    map<P, ll> d;
    vector<ll> st;
    bool flag = false;
    auto dfs = [&](auto dfs, ll par, ll root = -1, ll stop) -> void {
        if (flag) return;
        if (par == stop) flag = true;
        st.emplace_back(par);

        rep_e(chi, g[par]) {
            if (chi == root) continue;
            dfs(dfs, chi, par, stop);
        }

        if (flag) return;
        st.pop_back();
    };

    rep(i, m - 1) {
        flag = false;
        st.clear();
        dfs(dfs, a[i], -1, a[i + 1]);

        rep(i, st.size() - 1) {
            ll l = st[i];
            ll r = st[i + 1];
            if (l > r) swap(l, r);
            d[P(l, r)]++;
        }
    }

    ll t = 0;
    vector<ll> b;
    for (auto [key, val] : d) {
        b.emplace_back(val);
        t += val;
    }
    ll tmp = b.size();
    rep(i, n - 1 - tmp) b.emplace_back(0);

    m = b.size();
    ll s = 100100;
    vector dp(m + 1, vector(s, mint(0)));
    dp[0][0] = 1;
    rep(i, m) {
        rep(j, s) {
            // 使う
            if (j + b[i] < s) dp[i + 1][j + b[i]] += dp[i][j];

            // 使わない
            dp[i + 1][j] += dp[i][j];
        }
    }

    if (k + t < 0 or (k + t) % 2 == 1)
        cout << 0 << "\n";
    else
        cout << dp[m][(k + t) / 2].val() << "\n";

    return 0;
}