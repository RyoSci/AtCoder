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

ll h, w;

vector<ll> par;

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

bool same(ll x, ll y) { return root(x) == root(y); }

void unite(ll x, ll y) {
    ll px = root(x);
    ll py = root(y);
    if (px == py) return;
    if (px > py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

ll cal(ll x, ll y) { return x * w + y; }

int main() {
    cin >> h >> w;
    par.resize(h * w, -1);

    return 0;
}