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
    ll a, b, c;
    cin >> a >> b >> c;
    // dp[i][j][k]=i,j,k個から操作終了までの期待値
    vector<vector<vector<double>>> dp(
        101, vector<vector<double>>(101, vector<double>(101, 0.0)));

    rep_r(i, 100, -1) {
        rep_r(j, 100, -1) {
            rep_r(k, 100, -1) {
                if (0 <= i - 1 && j != 100 && k != 100) {
                    dp[i - 1][j][k] +=
                        (dp[i][j][k] + 1) * (i - 1.0) / (i - 1.0 + j + k);
                }
                if (0 <= j - 1 && k != 100 && i != 100) {
                    dp[i][j - 1][k] +=
                        (dp[i][j][k] + 1) * (j - 1.0) / (i + j - 1.0 + k);
                }
                if (0 <= k - 1 && i != 100 && j != 100) {
                    dp[i][j][k - 1] +=
                        (dp[i][j][k] + 1) * (k - 1.0) / (i + j + k - 1.0);
                }
            }
        }
    }
    // cout << 1.0 / (0 + 0 + 1 - 1.0) << "\n";

    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << dp[a][b][c] << endl;
    return 0;
}
