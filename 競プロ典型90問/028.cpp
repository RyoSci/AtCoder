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

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> grid(2000, vector<ll>(2000, 0));

    rep(i, n) {
        ll lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;
        grid[lx][ly] += 1;
        grid[lx][ry] -= 1;
        grid[rx][ly] -= 1;
        grid[rx][ry] += 1;
    }
    rep_s(i, 0, 2000) rep_s(j, 1, 2000) { grid[i][j] += grid[i][j - 1]; }

    rep_s(i, 1, 2000) rep_s(j, 0, 2000) { grid[i][j] += grid[i - 1][j]; }

    vector<ll> ans(n + 1, 0);
    rep(i, 2000) rep(j, 2000) { ans[grid[i][j]]++; }

    rep_s(i, 1, n + 1) cout << ans[i] << "\n";
    return 0;
}