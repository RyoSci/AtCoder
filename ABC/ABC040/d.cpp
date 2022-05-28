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

vector<ll> par(1e5 + 10, -1);

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

void unite(ll x, ll y) {
    ll px = root(x);
    ll py = root(y);
    if (px == py) return;
    if (px > py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<tuple<ll, ll, ll, ll>> tot_e;
    rep(i, m) {
        ll a, b, y;
        cin >> a >> b >> y;
        a--, b--;
        tot_e.emplace_back(make_tuple(-y, 1, a, b));
    }
    ll q;
    cin >> q;
    rep(i, q) {
        ll v, w;
        cin >> v >> w;
        v--;
        tot_e.emplace_back(make_tuple(-w, 0, v, i));
    }

    sort(tot_e.begin(), tot_e.end());

    vector<ll> ans(q, 0);

    rep_e(e, tot_e) {
        auto [y, i, a, b] = e;
        if (i == 0)
            ans[b] = -par[root(a)];
        else {
            unite(a, b);
        }
    }

    rep(i, q) cout << ans[i] << "\n";
    return 0;
}