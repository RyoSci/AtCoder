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
    if (n % 2 == 1) {
        a.emplace_back(-INF);
    }

    ll nn = (n + 1) / 2;
    vector dp(nn + 1, vector(3, vector(2, -INF)));
    dp[0][0][0] = 0;
    dp[0][1][0] = 0;

    rep(i, nn) {
        // スキップ
        rep(j, 2) { chmax(dp[i + 1][2][1], dp[i][j][0]); }

        rep(k, 2) {
            chmax(dp[i + 1][0][k], dp[i][0][k] + a[i * 2 + 0]);
            chmax(dp[i + 1][1][k], dp[i][0][k] + a[i * 2 + 1]);
            chmax(dp[i + 1][1][k], dp[i][1][k] + a[i * 2 + 1]);
        }

        // 前回スキップした場合は遷移先が多い
        chmax(dp[i + 1][0][1], dp[i][2][1] + a[i * 2 + 0]);
        chmax(dp[i + 1][1][1], dp[i][2][1] + a[i * 2 + 1]);
    }

    ll ans = 0;
    if (n % 2 == 1)
        rep(j, 3) chmax(ans, dp[nn][j][1]);
    else
        rep(j, 3) chmax(ans, dp[nn][j][0]);

    cout << ans << "\n";
    return 0;
}