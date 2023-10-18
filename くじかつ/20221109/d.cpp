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

vector<vector<P>> g(100100);
vector<ll> dis(100100, INF);
void dfs(ll par, ll root) {
    rep_e(e, g[par]) {
        auto [chi, c] = e;
        if (chi == root) continue;
        dis[chi] = dis[par] + c;
        dfs(chi, par);
    }
    return;
}

int main() {
    ll n;
    cin >> n;
    rep(i, n - 1) {
        ll a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(P(b, c));
        g[b].emplace_back(P(a, c));
    }

    ll q, k;
    cin >> q >> k;
    k--;
    dis[k] = 0;
    dfs(k, -1);

    rep(i, q) {
        ll x, y;
        cin >> x >> y;
        x--;
        y--;
        ll ans = dis[x] + dis[y];
        cout << ans << "\n";
    }
    return 0;
}