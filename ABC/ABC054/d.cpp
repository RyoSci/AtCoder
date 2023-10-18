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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n, ma, mb;
    cin >> n >> ma >> mb;
    vector<ll> a(n), b(n), c(n);
    rep(i, n) cin >> a[i] >> b[i] >> c[i];
    vector<vector<vector<ll>>> dp(
        n + 1, vector<vector<ll>>(410, vector<ll>(410, INF)));
    dp[0][0][0] = 0;
    rep_s(i, 1, n + 1) {
        rep(j, 401) {
            rep(k, 401) {
                if (j - a[i - 1] >= 0 && k - b[i - 1] >= 0)
                    chmin(dp[i][j][k],
                          dp[i - 1][j - a[i - 1]][k - b[i - 1]] + c[i - 1]);
                chmin(dp[i][j][k], dp[i - 1][j][k]);
            }
        }
    }

    ll ans = INF;
    rep_s(j, 1, 401) rep_s(k, 1, 401) {
        if (mb * j == ma * k) chmin(ans, dp[n][j][k]);
    }
    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";
    return 0;
}