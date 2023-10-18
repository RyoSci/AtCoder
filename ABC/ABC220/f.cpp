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
    ll n;
    cin >> n;
    vector<vector<ll>> g(n);
    rep(i, n - 1) {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].emplace_back(v);
        g[v].emplace_back(u);
    }

    vector<ll> dp(n, 0);
    vector<ll> dis(n, 0);

    auto dfs = [&](auto dfs, ll par, ll root = -1) -> ll {
        ll cnt = 0;
        rep_e(chi, g[par]) {
            if (chi == root) continue;
            dis[chi] = dis[par] + 1;
            cnt += dfs(dfs, chi, par);
        }

        return dp[par] = cnt + 1;
    };

    dfs(dfs, 0);
    vector<ll> ans(n, 0);
    rep(i, n) ans[0] += dis[i];

    auto dfs1 = [&](auto dfs1, ll par, ll root = -1) -> void {
        rep_e(chi, g[par]) {
            if (chi == root) continue;
            ans[chi] += ans[par];
            ans[chi] -= (dp[chi] - 1);
            ans[chi] += n - 2 - (dp[chi] - 1);
            dfs1(dfs1, chi, par);
        }
    };

    dfs1(dfs1, 0);

    for (auto a : ans) cout << a << " ";
    cout << endl;

    return 0;
}