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
#define INF (1LL << 60)
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

void chmax(ll &x, ll y) { x = max(x, y); }

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    vector dp(n, vector(2, vector(3, -INF)));
    dp[0][0][1] = 0;
    dp[0][1][0] = a[0];

    rep(i, n - 1) {
        // 使う場合
        chmax(dp[i + 1][1][0], dp[i][0][0] + a[i + 1]);
        chmax(dp[i + 1][1][1], dp[i][0][1] + a[i + 1]);
        chmax(dp[i + 1][1][2], dp[i][0][2] + a[i + 1]);

        // chmax(dp[i+1][1][0], dp[i][1][0]+a[i+1]);
        // chmax(dp[i+1][1][1], dp[i][1][1]+a[i+1]);
        // chmax(dp[i+1][1][2], dp[i][1][2]+a[i+1]);

        // 使わない場合
        chmax(dp[i + 1][0][1], dp[i][0][0]);
        chmax(dp[i + 1][0][2], dp[i][0][1]);
        // chmax(dp[i+1][0][3], dp[i][0][2]);

        chmax(dp[i + 1][0][0], dp[i][1][0]);
        chmax(dp[i + 1][0][1], dp[i][1][1]);
        chmax(dp[i + 1][0][2], dp[i][1][2]);
    }
    ll ans = -INF;
    if (n % 2) {
        rep(j, 2) rep_s(k, 1, 3) chmax(ans, dp[n - 1][j][k]);
    } else {
        rep(j, 2) rep(k, 2) chmax(ans, dp[n - 1][j][k]);
    }
    cout << ans << "\n";

    return 0;
}