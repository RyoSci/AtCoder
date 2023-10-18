// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
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

vector<vector<ll>> g(1001001);

vector<ll> seen(1001001, 0);

vector<P> ans;

void dfs(ll par, ll root = -1) {
    rep_e(chi, g[par]) {
        // if(chi==root) continue;
        if (seen[chi] == 1) continue;
        seen[chi] = 1;
        ans.emplace_back(P(par + 1, chi + 1));
        dfs(chi, par);
    }
}

int main() {
    ll n, m;
    cin >> n >> m;
    rep(i, m) {
        ll u, v;
        cin >> u >> v;
        u--;
        v--;
        g[u].emplace_back(v);
        g[v].emplace_back(u);
    }
    seen[0] = 1;
    dfs(0);
    rep(i, n - 1) { cout << ans[i].first << ' ' << ans[i].second << "\n"; }

    ans.clear();
    rep(i, 1001001) seen[i] = 0;

    queue<ll> q;
    q.emplace(0);
    seen[0] = 1;
    while (q.size() > 0) {
        ll par = q.front();
        q.pop();
        rep_e(chi, g[par]) {
            if (seen[chi] == 1) continue;
            ans.emplace_back(P(par + 1, chi + 1));
            seen[chi] = 1;
            q.emplace(chi);
        }
    }

    rep(i, n - 1) { cout << ans[i].first << ' ' << ans[i].second << "\n"; }
    return 0;
}