// #define _GLIBCXX_DEBUG
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
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

vector<ll> par;

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

bool same(ll x, ll y) { return find(x) == find(y); }

void unite(ll x, ll y) {
    if (same(x, y)) return;
    ll px = find(x);
    ll py = find(y);
    if (px > py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

int main() {
    ll n;
    cin >> n;
    par.resize(n, -1);

    vector<P> x(n), y(n);
    for (ll i = 0; i < n; i++) {
        cin >> x[i].first >> y[i].first;
        x[i].second = i;
        y[i].second = i;
    }

    // 隣を飛び越えるのは不必要
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    vector<tuple<ll, ll, ll>> xy;
    rep(i, n - 1) {
        ll a, b, c;
        a = x[i + 1].first - x[i].first;
        b = x[i + 1].second;
        c = x[i].second;
        xy.push_back(make_tuple(a, b, c));
        a = y[i + 1].first - y[i].first;
        b = y[i + 1].second;
        c = y[i].second;
        xy.push_back(make_tuple(a, b, c));
    }

    sort(xy.begin(), xy.end());

    ll ans = 0;
    // 最小全域木を求める
    rep_e(e, xy) {
        ll a, b, c;
        tie(a, b, c) = e;
        if (same(b, c)) continue;
        unite(b, c);
        ans += a;
    }

    cout << ans << "\n";
    return 0;
}