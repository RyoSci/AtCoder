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
using lli = long long;
// using mint = modint1000000007;
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, q;
        cin >> n >> q;
        ll m = 1100;
        // ll m = 10;
        vector<vector<ll>> grid(m, vector<ll>(m, 0));
        rep(i, n) {
            ll h, w;
            cin >> h >> w;
            grid[h + 1][w + 1] += h * w;
        }

        rep(i, m - 1) rep(j, m - 1) {
            grid[i + 1][j + 1] += grid[i + 1][j] + grid[i][j + 1] - grid[i][j];
        }
        // rep(i, m) {
        //     for (auto a : grid[i]) cout << a << " ";
        //     cout << endl;
        // }

        rep(i, q) {
            ll hs, ws, hb, wb;
            cin >> hs >> ws >> hb >> wb;
            hs++;
            ws++;
            ll ans = grid[hb][wb] - grid[hs][wb] - grid[hb][ws] + grid[hs][ws];
            cout << ans << "\n";
        }
    }
    return 0;
}