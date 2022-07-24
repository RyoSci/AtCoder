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
    ll n, c;
    cin >> n >> c;
    vector<ll> t(n), a(n);
    for (ll i = 0; i < n; i++) cin >> t[i] >> a[i];

    vector<vector<vector<ll>>> dp(30,
                                  vector<vector<ll>>(n + 1, vector<ll>(2, 0)));
    rep(i, 30) dp[i][0][1] = 1;

    rep(i, 30) rep(j, n) {
        if (t[j] == 1) {
            dp[i][j + 1][0] = dp[i][j][0] & (a[j] >> i & 1);
            dp[i][j + 1][1] = dp[i][j][1] & (a[j] >> i & 1);
        } else if (t[j] == 2) {
            dp[i][j + 1][0] = dp[i][j][0] | (a[j] >> i & 1);
            dp[i][j + 1][1] = dp[i][j][1] | (a[j] >> i & 1);
        } else {
            dp[i][j + 1][0] = dp[i][j][0] ^ (a[j] >> i & 1);
            dp[i][j + 1][1] = dp[i][j][1] ^ (a[j] >> i & 1);
        }
    }

    ll ans = c;
    rep(i, n) {
        ll tmp = 0;
        rep(j, 30) { tmp += dp[j][i + 1][ans >> j & 1] << j; }
        ans = tmp;
        cout << ans << "\n";
    }
    return 0;
}