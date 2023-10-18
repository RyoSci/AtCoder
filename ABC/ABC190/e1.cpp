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

void chmin(ll &x, ll y) {
    x = min(x, y);
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }
    ll k;
    cin >> k;
    vector<ll> c(k);
    map<ll, ll> cs;
    for (ll i = 0; i < k; i++) {
        cin >> c[i];
        c[i]--;
        cs[c[i]] = i;
    }

    vector dis(k, vector(k, INF));

    rep(i, k) {
        dis[i][i] = 0;
        queue<P> q;
        q.emplace(P(c[i], dis[i][i]));
        vector<bool> seen(n, 0);

        while (q.size()) {
            auto [par, d] = q.front();
            seen[par] = 1;
            if (cs.count(par) > 0) chmin(dis[i][cs[par]], d);
            q.pop();
            // printf("%d %d %d\n", i, par, d);
            rep_e(chi, g[par]) {
                if (seen[chi]) continue;
                q.emplace(P(chi, d + 1));
            }
        }
    }
    vector dp(1 << k, vector(k, INF));

    rep(i, k) { dp[1 << i][i] = 1; }

    rep(i, 1 << k) {
        rep(from, k) {
            if (dp[i][from] == INF) continue;
            if (((i >> from) & 1) == 0) continue;
            rep(to, k) {
                chmin(dp[i | (1 << to)][to], dp[i][from] + dis[from][to]);
            }
        }
    }

    ll ans = INF;
    rep(i, k) chmin(ans, dp[(1 << k) - 1][i]);

    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";

    // rep(i, k) {
    //     for (auto a : dis[i]) cout << a << " ";
    //     cout << endl;
    // }

    return 0;
}