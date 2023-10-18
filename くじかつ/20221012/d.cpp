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

vector<ll> cnt(2000000, 0);
vector<vector<ll>> g(2000000);

void dfs(ll par, ll root = -1) {
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        cnt[chi] += cnt[par];
        dfs(chi, par);
    }
}

int main() {
    ll n, q;
    cin >> n >> q;

    cnt.resize(n);

    vector<ll> a(n - 1), b(n - 1);
    for (ll i = 0; i < n - 1; i++) cin >> a[i] >> b[i];
    vector<ll> p(q), x(q);
    for (ll i = 0; i < q; i++) cin >> p[i] >> x[i];

    rep(i, n - 1) {
        g[a[i] - 1].emplace_back(b[i] - 1);
        g[b[i] - 1].emplace_back(a[i] - 1);
    }

    rep(i, q) { cnt[p[i] - 1] += x[i]; }

    dfs(0);

    for (auto a : cnt) cout << a << " ";
    cout << endl;

    return 0;
}