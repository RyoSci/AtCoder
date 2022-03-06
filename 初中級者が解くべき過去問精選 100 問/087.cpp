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

vector<ll> par(100000 + 10, -1);

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

void unite(ll x, ll y) {
    ll px = find(x);
    ll py = find(y);
    if (px == py) return;
    par[px] += par[py];
    par[py] = px;
    return;
}

bool same(ll x, ll y) { return find(x) == find(y); }

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(m), b(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i];
    ll now = n * (n - 1) / 2;
    vector<ll> ans(m);

    rep_r(i, m - 1, -1) {
        ans[i] = now;
        a[i]--;
        b[i]--;
        if (!same(a[i], b[i])) {
            now -= par[find(a[i])] * par[find(b[i])];
            unite(a[i], b[i]);
        }
    }

    rep(i, m) { cout << ans[i] << "\n"; }
    return 0;
}