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
    ll n, m, p;
    cin >> n >> m >> p;
    vector<vector<P>> g(n);

    rep(i, m) {
        ll a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(P(b, c));
    }

    vector dp(n, vector(6 * n + 100, -INF));
    dp[0][0] = 0;

    queue<P> q;
    q.emplace(P(0, 0));

    auto bfs = [&](ll limit) {
        while (1) {
            if (q.size() == 0) break;
            auto [par, t] = q.front();
            if (t == limit) break;
            q.pop();
            for (auto [chi, c] : g[par]) {
                if (dp[chi][t + 1] < dp[par][t] + c) {
                    dp[chi][t + 1] = dp[par][t] + c;
                    q.emplace(P(chi, t + 1));
                }
            }
        }
    };

    bfs(2 * n + 10);

    vector seen(n, vector(n, false));
    rep(i, n) {
        seen[i][i] = true;
        queue<ll> qq;
        qq.emplace(i);
        while (qq.size()) {
            ll par = qq.front();
            qq.pop();
            for (auto [chi, c] : g[par]) {
                if (seen[i][chi]) continue;
                seen[i][chi] = true;
                qq.emplace(chi);
            }
        }
    }

    rep(i, n) {
        if (seen[0][i] and seen[i][n - 1]) {
            ll ans0 = -INF;
            ll ans1 = -INF;
            rep(j, n) ans0 = max(ans0, dp[i][j] - j * p);
            rep(j, 2 * n) ans1 = max(ans1, dp[i][j] - j * p);
            if (ans0 < ans1) {
                cout << -1 << "\n";
                return 0;
            }
        }
    }

    ll ans = -INF;
    rep(i, 2 * n + 10) { ans = max(ans, dp[n - 1][i] - i * p); }
    cout << max(ans, 0) << "\n";

    return 0;
}