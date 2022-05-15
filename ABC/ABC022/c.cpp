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
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> g(n, vector<ll>(n, INF));
    rep(i, m) {
        ll u, v, l;
        cin >> u >> v >> l;
        u--, v--;
        g[u][v] = l, g[v][u] = l;
    }

    ll ans = INF;
    rep(v, g[0].size()) {
        ll l;
        vector<ll> dis(n, INF);
        vector<ll> seen(n, 0);
        l = g[0][v];
        if (l == INF) continue;
        dis[v] = 0;
        g[0][v] = INF;
        g[v][0] = INF;
        while (1) {
            ll now = 0;
            ll cnt = INF;
            rep(i, n) {
                if (seen[i])
                    continue;
                else {
                    if (cnt > dis[i]) {
                        now = i;
                        cnt = dis[i];
                    }
                }
            }
            if (cnt == INF) break;
            seen[now] = 1;
            rep(i, n) { dis[i] = min(dis[i], dis[now] + g[now][i]); }
        }
        ans = min(ans, l + dis[0]);
        g[0][v] = l;
        g[v][0] = l;
    }

    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";

    return 0;
}