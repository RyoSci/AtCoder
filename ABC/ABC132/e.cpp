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
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> g(n);
    rep(i, m) {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].emplace_back(v);
    }

    ll s, t;
    cin >> s >> t;
    s--;
    t--;

    vector dp(n, vector(3, INF));
    dp[s][0] = 0;

    queue<P> q;
    q.emplace(P(s, 0));
    while (q.size()) {
        auto [par, state] = q.front();
        q.pop();
        rep_e(chi, g[par]) {
            if (dp[chi][(state + 1) % 3] > dp[par][state] + 1) {
                dp[chi][(state + 1) % 3] = dp[par][state] + 1;
                q.emplace(P(chi, (state + 1) % 3));
            }
        }
    }
    if (dp[t][0] == INF)
        cout << -1 << "\n";
    else
        cout << dp[t][0] / 3 << "\n";
    return 0;
}