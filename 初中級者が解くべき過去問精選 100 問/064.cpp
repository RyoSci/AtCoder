#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

vector<ll> par;

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

bool same(ll x, ll y) { return root(x) == root(y); }

void unite(ll x, ll y) {
    ll px = root(x);
    ll py = root(y);
    if (same(px, py)) return;
    par[px] += par[py];
    par[py] = px;
    return;
}

int main() {
    ll v, e;
    cin >> v >> e;
    vector<tuple<ll, ll, ll>> stw;
    rep(i, e) {
        ll s, t, w;
        cin >> s >> t >> w;
        stw.push_back(make_tuple(w, s, t));
    }

    sort(stw.begin(), stw.end());

    par.resize(v, -1);
    ll ans = 0;
    rep(i, e) {
        ll w, s, t;
        tie(w, s, t) = stw[i];
        if (same(s, t))
            continue;
        else {
            unite(s, t);
            ans += w;
        }
    }
    cout << ans << "\n";
    return 0;
}