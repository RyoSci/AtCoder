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

bool chmax(ll &x, ll y) {
    if (x < y) {
        x = y;
        return true;
    }
    return false;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> a(2 * n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    for (ll i = 0; i < n; i++) a[i + n] = a[i];
    vector<vector<vector<ll>>> dp(2 * n,
                                  vector<vector<ll>>(2 * n, vector<ll>(2, 0)));
    // dp[i][j][k]=左端がiで右端かjの時の区間になった時のJの最大スコア
    // dp[i][j][0] -> dp[i+1][j][1] or dp[i][j-1][1] への遷移がある
    // dp[i+1][j][1] or dp[i][j-1][1] Jへの遷移もある
    // 区間を縮めていく l, r
    // が現在の左端、右端なので各分岐でどこを使ったかを気をつけながらa[]を足す

    // 初期化、２倍の長さにして円の処理を簡略化
    rep(i, n) { dp[i + 1][i + n - 1][0] = a[i]; }

    rep_r(i, n - 1, 0) {
        rep_s(l, 0, n + 1) {
            ll r = l + i;
            // if (dp[l][r][0] == 0) continue;
            if (a[l] > a[r]) {
                chmax(dp[l + 1][r][1], dp[l][r][0]);
                // 右端と左端を遷移
                if (l + 2 < 2 * n)
                    chmax(dp[l + 2][r][0], dp[l + 1][r][1] + a[l + 1]);
                chmax(dp[l + 1][r - 1][0], dp[l + 1][r][1] + a[r]);

            } else {
                chmax(dp[l][r - 1][1], dp[l][r][0]);
                // 右端と左端を遷移
                chmax(dp[l + 1][r - 1][0], dp[l][r - 1][1] + a[l]);
                if (r - 2 >= 0)
                    chmax(dp[l][r - 2][0], dp[l][r - 1][1] + a[r - 1]);
            }
        }
    }

    ll ans = 0;
    rep(i, 2 * n) {
        for (auto a : dp[i]) cout << a[0] << " ";
        cout << endl;
        rep(j, 2 * n) { chmax(ans, dp[i][j][0]); }
    }
    cout << ans << "\n";
    return 0;
}