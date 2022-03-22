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

int main() {
    string t;
    cin >> t;
    ll n = t.length();
    vector<ll> s(n, 0);
    rep(i, n) { s[i] = t[i] - '0'; }

    ll k;
    cin >> k;

    vector<vector<vector<vector<ll>>>> dp(
        n, vector<vector<vector<ll>>>(
               10, vector<vector<ll>>(k + 1, vector<ll>(2, 0))));

    // dp[i][j][k][l] =
    // 上からi桁目の数字がjである時に0でない数字がちょうどk個あって、
    // sと上からi桁が一致しているかどうかl(true/false)の時の場合の数

    dp[0][s[0]][1][1] = 1;
    dp[0][0][0][0] = 1;
    rep_s(j, 1, 10) {
        if (j < s[0]) dp[0][j][1][0] = 1;
    }

    rep(i, n - 1) {
        rep(j, 10) {
            rep(kk, k + 1) {
                // l==0のときは次の桁は何を選んでもよいが、k+1を超えるような数をは選んではいけない
                rep(m, 10) {
                    if (m == 0)
                        dp[i + 1][0][kk][0] += dp[i][j][kk][0];
                    else if (kk + 1 <= k)
                        dp[i + 1][m][kk + 1][0] += dp[i][j][kk][0];
                }

                // l==1のときは次の桁の一致しているか、していないかの場合があり、それぞれk+1を超えるような数をは選んではいけない
                rep(m, 10) {
                    if (s[i + 1] == m) {
                        if (m == 0)
                            dp[i + 1][m][kk][1] += dp[i][j][kk][1];
                        else if (kk + 1 <= k)
                            dp[i + 1][m][kk + 1][1] += dp[i][j][kk][1];
                    } else if (s[i + 1] > m) {
                        if (m == 0)
                            dp[i + 1][m][kk][0] += dp[i][j][kk][1];
                        else if (kk + 1 <= k) {
                            dp[i + 1][m][kk + 1][0] += dp[i][j][kk][1];
                        }
                    }
                }
            }
        }
    }

    ll ans = 0;
    rep(j, 10) {
        rep(l, 2) { ans += dp[n - 1][j][k][l]; }
    }
    cout << ans << "\n";

    return 0;
}