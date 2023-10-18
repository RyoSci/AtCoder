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

vector<vector<ll>> g;
set<ll> s;

void dfs(ll par, ll root, ll rest) {
    if (rest == 0) {
        return;
    };
    rep_e(chi, g[par]) {
        if (chi != root) {
            s.insert(chi + 1);
            dfs(chi, par, rest - 1);
        }
    }
}

int main() {
    ll n, m;
    cin >> n >> m;
    g.resize(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    ll q;
    cin >> q;
    rep(i, q) {
        ll x, k;
        cin >> x >> k;
        x--;
        s.clear();
        s.insert(x + 1);
        dfs(x, -1, k);
        ll ans = 0;
        rep_e(e, s) ans += e;
        cout << ans << "\n";
    }
    return 0;
}