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

vector<vector<ll>> table(16, vector<ll>(16, 1));
vector<vector<ll>> g(16);

void dfs(ll par, ll root = -1) {
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        table[par][chi] = 0;
        dfs(chi, par);
    }
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> x(m), y(m);
    rep(i, m) cin >> x[i] >> y[i];

    rep(i, m) { g[y[i] - 1].push_back(x[i] - 1); }

    rep(i, n) { dfs(i); }

    vector<ll> dp(1 << n, 0);
    dp[0] = 1;
    // dp[i]:=集合iが既に矛盾なく到着している時の場合の数
    rep(i, 1 << n) {
        rep(j, n) {
            if (i >> j & 1) continue;
            bool ok = true;
            rep(k, n) {
                if ((i >> k) & 1 && table[k][j] == 0) ok = false;
            }
            if (ok) dp[i | 1 << j] += dp[i];
        }
    }

    cout << dp[(1 << n) - 1] << "\n";

    return 0;
}