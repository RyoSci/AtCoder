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
    ll n, m, x, y;
    cin >> n >> m >> x >> y;
    x--;
    y--;

    vector<ll> a(m), b(m), t(m), k(m);
    rep(i, m) cin >> a[i] >> b[i] >> t[i] >> k[i];
    vector<vector<T>> g(n);
    rep(i, m) {
        a[i]--;
        b[i]--;
        g[a[i]].emplace_back(T(b[i], t[i], k[i]));
        g[b[i]].emplace_back(T(a[i], t[i], k[i]));
    }

    vector<ll> cost(n, INF);
    cost[x] = 0;

    priority_queue<P> q;
    q.push(P(0, x));

    while (q.size() > 0) {
        auto [c, node] = q.top();
        q.pop();
        c = -c;
        if (cost[node] < c) continue;
        rep_e(e, g[node]) {
            auto [to, ti, ki] = e;
            ll nc = (c + ki - 1) / ki * ki + ti;
            if (cost[to] > nc) {
                cost[to] = nc;
                q.push(P(-nc, to));
            }
        }
    }

    if (cost[y] == INF)
        cout << -1 << "\n";
    else
        cout << cost[y] << "\n";

    return 0;
}