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
    ll n, u, v;
    cin >> n >> u >> v;
    u--;
    v--;
    vector<vector<ll>> g(n);
    rep(i, n - 1) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    vector<ll> dp(n, 0);
    auto dfs = [&](auto dfs, ll par, ll root) -> void {
        rep_e(chi, g[par]) {
            if (chi == root) continue;
            dfs(dfs, chi, par);
            dp[par] = max(dp[par], dp[chi] + 1);
        }
    };

    dfs(dfs, v, -1);

    auto dfs1 = [&](auto dfs1, ll par, ll root, vector<ll> &dis) -> void {
        rep_e(chi, g[par]) {
            if (chi == root) continue;
            dis[chi] = dis[par] + 1;
            dfs1(dfs1, chi, par, dis);
        }
    };

    vector<ll> dis_aoki(n, INF);
    dis_aoki[v] = 0;
    dfs1(dfs1, v, -1, dis_aoki);

    vector<ll> dis_taka(n, INF);
    dis_taka[u] = 0;
    dfs1(dfs1, u, -1, dis_taka);

    ll ans = 0;
    rep(i, n) {
        if (dis_aoki[i] <= dis_taka[i]) continue;
        ll d = dis_aoki[u] - 2 * dis_taka[i];
        ll res = dis_taka[i] + dp[i] + d - 1;
        ans = max(res, ans);
    }

    cout << ans << "\n";

    return 0;
}