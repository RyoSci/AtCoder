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
using mint = modint1000000007;
// using mint = modint998244353;
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
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    vector<ll> dis(n, INF);
    vector<mint> dp(n, 0);
    dis[0] = 0;
    dp[0] = 1;
    queue<ll> q;
    q.emplace(0);
    while (q.size()) {
        ll par = q.front();
        q.pop();
        rep_e(chi, g[par]) {
            if (dis[chi] > dis[par] + 1) {
                dis[chi] = dis[par] + 1;
                dp[chi] += dp[par];
                q.emplace(chi);
            } else if (dis[chi] == dis[par] + 1) {
                dp[chi] += dp[par];
            }
        }
    }

    cout << dp[n - 1].val() << "\n";
    return 0;
}