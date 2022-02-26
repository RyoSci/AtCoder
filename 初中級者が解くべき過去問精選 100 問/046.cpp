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
#define _GLIBCXX_DEBUG

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> r(n), c(n);
    for (ll i = 0; i < n; i++) cin >> r[i] >> c[i];

    // vector<vector<vector<ll>>> dp(n, vector<vector<ll>>(n, vector<ll>(n,
    // INF)));
    vector<vector<ll>> dp(n, vector<ll>(n, INF));

    // dp[i][j][k]<-区間の大きさがiの時に区間がj番目からk番目の時のスコアの最小値
    rep(i, n) { dp[i][i] = 0; }

    rep(i, n + 1) {
        rep(j, n) {
            if (i + j > n) continue;
            rep_s(k, j, j + i - 1) {
                chmin(dp[j][j + i - 1], dp[j][k] + dp[k + 1][j + i - 1] +
                                            r[j] * c[j + i - 1] * c[k]);
            }
        }
    }
    cout << dp[0][n - 1] << "\n";
    return 0;
}