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

    vector<vector<P>> g(n);
    rep(i, m) {
        ll a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(P{b, c});
        g[b].emplace_back(P{a, c});
    }

    priority_queue<P> q;
    vector<ll> dis(n, INF);
    dis[0] = 0;
    q.emplace(P{-dis[0], 0});

    while (q.size() > 0) {
        auto [d, par] = q.top();
        q.pop();
        d = -d;

        if (d > dis[par]) continue;
        for (auto [chi, c] : g[par]) {
            if (dis[chi] > dis[par] + c) {
                dis[chi] = dis[par] + c;
                q.emplace(P{-dis[chi], chi});
            }
        }
    }

    priority_queue<P> q1;
    vector<ll> dis1(n, INF);
    dis1[n - 1] = 0;
    q1.emplace(P{-dis1[n - 1], n - 1});

    while (q1.size() > 0) {
        auto [d, par] = q1.top();
        q1.pop();
        d = -d;

        if (d > dis1[par]) continue;
        for (auto [chi, c] : g[par]) {
            if (dis1[chi] > dis1[par] + c) {
                dis1[chi] = dis1[par] + c;
                q1.emplace(P{-dis1[chi], chi});
            }
        }
    }

    rep(k, n) {
        ll ans = dis[k] + dis1[k];
        cout << ans << "\n";
    }

    return 0;
}