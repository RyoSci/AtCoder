// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
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
// using mint = modint1000000007;
using mint = modint998244353;
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

vector<ll> seen(2 * 101010, 0);
vector<ll> par(2 * 101010, -1);
vector<vector<ll>> g(2 * 101010);

ll find(ll x) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x]);
}

bool unite(ll x, ll y) {
    ll px = find(x);
    ll py = find(y);
    if (px == py) return true;
    par[px] += par[py];
    par[py] = px;
    return false;
}

ll dfs(ll x, ll root = -1) {
    seen[x] = 1;
    ll cnt = 0;
    rep_e(chi, g[x]) {
        if (root == chi) continue;
        if (unite(chi, x))
            cnt++;
        else
            cnt += dfs(chi, x);
    }
    return cnt;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> u(m), v(m);
    for (ll i = 0; i < m; i++) {
        cin >> u[i] >> v[i];
        u[i]--;
        v[i]--;
        g[u[i]].push_back(v[i]);
        g[v[i]].push_back(u[i]);
    }

    ll cnt = 0;
    rep(i, n) {
        if (!seen[i]) {
            if (dfs(i) == 2)
                cnt++;
            else {
                cout << 0 << "\n";
                return 0;
            }
        }
    }

    mint ans;
    ans = mint(2).pow(cnt);
    cout << ans.val() << "\n";

    return 0;
}