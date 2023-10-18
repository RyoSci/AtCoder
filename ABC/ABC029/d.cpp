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

ll dp[15][2][15];

int main() {
    string n;
    cin >> n;
    ll m = n.length();
    // dp[i][j][k]:=i桁目がis_smaller j
    // の時のそれまでの１の数の合計がk個の時の場合の数
    dp[0][0][0] = 1;

    rep(i, m) {
        rep(k, 10) {
            // smaller
            dp[i + 1][1][k] += dp[i][1][k] * 9;
            dp[i + 1][1][k + 1] += dp[i][1][k] * 1;
            // not smaller
            rep(j, 10) {
                if (j < n[i] - '0') {
                    if (j == 1)
                        dp[i + 1][1][k + 1] += dp[i][0][k];
                    else
                        dp[i + 1][1][k] += dp[i][0][k];
                } else if (j == n[i] - '0') {
                    if (j == 1)
                        dp[i + 1][0][k + 1] += dp[i][0][k];
                    else
                        dp[i + 1][0][k] += dp[i][0][k];
                }
            }
        }
    }

    ll ans = 0;
    rep(j, 2) {
        rep(k, 10) { ans += dp[m][j][k] * k; }
    }
    cout << ans << "\n";
    // rep(i, m + 1) {
    //     rep(j, 2) {
    //         for (auto a : dp[i][j]) cout << a << " ";
    //         cout << endl;
    //     }
    // }
    return 0;
}