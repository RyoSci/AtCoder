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

vector<vector<ll>> g(100000 + 10);
vector<ll> dis(100000 + 10, 0);

void dfs(ll par, ll root = -1) {
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        dis[chi] = dis[par] + 1;
        dfs(chi, par);
    }
    return;
}

int main() {
    ll n;
    cin >> n;
    rep(i, n - 1) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    dfs(0);
    ll index = 0;
    rep(i, n) {
        if (dis[index] < dis[i]) {
            index = i;
        }
    }

    rep(i, n) dis[i] = 0;
    dfs(index);
    index = 0;
    rep(i, n) {
        if (dis[index] < dis[i]) {
            index = i;
        }
    }

    cout << dis[index] + 1 << "\n";

    return 0;
}