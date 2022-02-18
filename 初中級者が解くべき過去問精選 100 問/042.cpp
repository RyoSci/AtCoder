#include <algorithm>
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
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> d(n);
    rep(i, n) { cin >> d[i]; }
    vector<ll> c(m);
    rep(i, m) { cin >> c[i]; }

    vector<vector<ll>> dp(m + 1, vector<ll>(n + 1, INF));

    // dp[i][j]<-i日目にj番目の都市にいる時のコストの最小値
    // 遷移は次の都市に行く場合と、と止まる場合

    dp[0][0] = 0;
    rep(i, m) {
        rep(j, n) {
            if (dp[i][j] == INF) continue;
            // とどまる場合
            chmin(dp[i + 1][j], dp[i][j]);
            // 次の町に行く場合
            chmin(dp[i + 1][j + 1], dp[i][j] + c[i] * d[j]);
        }
    }

    ll ans = INF;
    rep(i, m + 1) { ans = min(ans, dp[i][n]); }
    cout << ans << "\n";
    rep(i, m + 1) {
        for (auto a : dp[i]) cout << a << " ";
        cout << endl;
    }
    return 0;
}