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
    for (ll i = 1; i < n; i++) {
        ll p;
        cin >> p;
        p--;
        g[p].emplace_back(i);
    }

    vector<ll> in(n, -1);
    vector<ll> out(n, -1);
    vector<ll> dis(n, INF);
    dis[0] = 0;
    ll k = 0;

    auto dfs = [&](auto dfs, ll par) -> void {
        in[par] = k;
        k++;
        rep_e(chi, g[par]) {
            if (dis[chi] != INF) continue;
            dis[chi] = dis[par] + 1;
            dfs(dfs, chi);
        }
        out[par] = k;
        k++;
    };

    dfs(dfs, 0);

    vector<vector<ll>> tree(n);

    rep(i, n) { tree[dis[i]].emplace_back(in[i]); }

    rep(i, n) { sort(tree[i].begin(), tree[i].end()); }

    ll q;
    cin >> q;
    rep(i, q) {
        ll u, d;
        cin >> u >> d;
        u--;
        auto l = lower_bound(tree[d].begin(), tree[d].end(), in[u]);
        auto r = upper_bound(tree[d].begin(), tree[d].end(), out[u]);

        cout << r - l << "\n";
    }
    return 0;
}