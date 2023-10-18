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

vector<ll> par(100000 + 10, -1);

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
    ll n, m, k;
    cin >> n >> m >> k;

    vector<ll> a(m), b(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i];

    vector<ll> c(k), d(k);
    for (ll i = 0; i < k; i++) cin >> c[i] >> d[i];

    vector<vector<ll>> friends(n);
    rep(i, m) {
        a[i]--;
        b[i]--;
        friends[a[i]].emplace_back(b[i]);
        friends[b[i]].emplace_back(a[i]);
        unite(a[i], b[i]);
    }

    vector<vector<ll>> blocks(n);
    rep(i, k) {
        c[i]--;
        d[i]--;
        blocks[c[i]].emplace_back(d[i]);
        blocks[d[i]].emplace_back(c[i]);
    }

    vector<ll> ans(n, 0);

    rep(i, n) {
        ll res = -par[root(i)] - friends[i].size() - 1;
        rep_e(j, blocks[i]) {
            if (root(i) == root(j)) res--;
        }
        ans[i] = res;
    }
    // rep(i, n) {
    //     for (auto a : friends[i]) cout << a << " ";
    //     cout << endl;
    //     for (auto a : blocks[i]) cout << a << " ";
    //     cout << endl;
    // }

    for (auto a : ans) cout << a << " ";
    cout << endl;

    return 0;
}