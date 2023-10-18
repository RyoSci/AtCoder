#define _GLIBCXX_DEBUG
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

int main() {
    ll n, a;
    cin >> n >> a;
    vector<ll> x(n);
    for (ll i = 0; i < n; i++) cin >> x[i];

    vector<vector<vector<ll>>> dp(
        n + 1, vector<vector<ll>>(50 + 1, vector<ll>(50 * 50 + 1, 0)));
    // dp[i][j][k]:=i番目までのカードを使った時に選んだカードの枚数がjの時の和がkの時の場合の数
    dp[0][0][0] = 1;
    rep(i, n) rep(j, 50) rep(k, 50 * 50 + 1) {
        // 使う場合
        ll tmp = k + x[i];
        if (tmp <= 50 * 50) dp[i + 1][j + 1][tmp] += dp[i][j][k];
        // 使わない場合
        dp[i + 1][j][k] += dp[i][j][k];
    }

    ll ans = 0;
    rep_s(j, 1, 51) rep(k, 50 * 50 + 1) {
        if (k == a * j) {
            ans += dp[n][j][k];
            // cout << dp[n][j][k] << ' ' << j << ' ' << k << "\n";
        }
    }
    cout << ans << "\n";
    return 0;
}