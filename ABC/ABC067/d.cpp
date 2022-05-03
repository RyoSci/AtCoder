#define _GLIBCXX_DEBUG
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

vector<vector<ll>> g;
vector<ll> colors;
vector<ll> pars;

void dfs(ll par, ll root = -1) {
    pars[par] = root;
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        dfs(chi, par);
    }
    return;
}

void dfs2(ll par, ll root = -1) {
    colors[par] = 1;
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        if (colors[chi] == 2) continue;
        dfs2(chi, par);
    }
    return;
}

int main() {
    ll n;
    cin >> n;
    g.resize(n);
    colors.resize(n, 0);
    pars.resize(n, -1);
    rep(i, n - 1) {
        ll a, b;
        cin >> a >> b;
        a--, b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    dfs(0);
    ll now = n - 1;
    vector<ll> path;
    while (now != 0) {
        path.emplace_back(now);
        now = pars[now];
    }
    path.emplace_back(now);
    reverse(path.begin(), path.end());
    ll m = path.size();
    rep(i, (m + 1) / 2) { colors[path[i]] = 1; }
    rep_s(i, (m + 1) / 2, m) { colors[path[i]] = 2; }

    dfs2(0);
    ll a = 0, b = 0;
    rep(i, n) {
        if (colors[i] == 1)
            a++;
        else
            b++;
    }
    if (a > b)
        cout << "Fennec"
             << "\n";
    else
        cout << "Snuke"
             << "\n";

    // for (auto a : colors) cout << a << " ";
    // cout << endl;
    return 0;
}