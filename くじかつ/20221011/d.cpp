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

vector<ll> par(2 * 100000 + 10, -1);

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

void unite(ll x, ll y) {
    ll px = find(x);
    ll py = find(y);
    if (px == py) return;
    if (px > py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

bool same(ll x, ll y) { return find(x) == find(y); }

int main() {
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    vector<ll> ans(n, 0);
    ll cnt = 0;
    rep_r(i, n - 1, -1) {
        ans[i] = cnt;
        rep_e(chi, g[i]) {
            if (chi > i) {
                if (same(chi, i)) continue;
                unite(chi, i);
                cnt--;
            }
        }
        cnt++;
    }

    for (auto a : ans) cout << a << " ";
    cout << endl;
    return 0;
}