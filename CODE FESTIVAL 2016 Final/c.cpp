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

vector<ll> par(1e6, -1);

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

void unite(ll x, ll y) {
    ll px = root(x);
    ll py = root(y);
    if (px == py) return;
    if (px < py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    ll k, l;
    rep(i, n) {
        cin >> k;
        rep(j, k) {
            cin >> l;
            l--;
            unite(i, l + n);
        }
    }

    bool ans = true;
    // 全員同じ親であれば良い
    rep(i, n) {
        if (root(0) != root(i)) ans = false;
    }
    cout << (ans ? "YES" : "NO") << "\n";
    return 0;
}