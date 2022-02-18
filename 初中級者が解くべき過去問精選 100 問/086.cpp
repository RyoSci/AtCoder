#include <algorithm>
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
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

vector<ll> par;

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

void unite(ll x, ll y) {
    ll px = find(x);
    ll py = find(y);
    if (px == py) return;
    if (par[px] > par[py]) swap(px, py);
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

    par.resize(n, -1);
    vector<ll> par_(n);
    par_ = par;

    ll ans = 0;
    rep(i, m) {
        par = par_;
        rep(j, m) {
            if (i == j) continue;
            unite(a[j] - 1, b[j] - 1);
        }
        if (!same(a[i] - 1, b[i] - 1)) ans++;
    }

    cout << ans << "\n";
    return 0;
}