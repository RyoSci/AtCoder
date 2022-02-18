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

vector<ll> par(10000, -1);

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

void unite(ll x, ll y) {
    ll px = find(x);
    ll py = find(y);
    if (px == py) return;
    if (par[px] < par[py]) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

bool same(ll x, ll y) { return find(x) == find(y); }

int main() {
    ll n, q;
    cin >> n >> q;

    par.resize(n, -1);
    rep(i, q) {
        ll c, x, y;
        cin >> c >> x >> y;
        if (c == 0)
            unite(x, y);
        else {
            if (same(x, y))
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
    }
    return 0;
}