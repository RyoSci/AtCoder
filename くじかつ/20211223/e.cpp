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
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int main() {
    Int h, w, k;
    cin >> h >> w >> k;
    Int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    Int mod = 998244353;
    vector<vector<Int>> dp(k + 1, vector<Int>(4));
    if (x1 == x2 && y1 == y2)
        dp[0] = {1, 1, 1, 0};
    else if (x1 == x2)
        dp[0] = {0, 1, 0, 0};
    else if (y1 == y2)
        dp[0] = {1, 0, 0, 0};
    else if (x1 != x2 && y1 != y2)
        dp[0] = {0, 0, 0, 1};
    rep(i, k) {
        dp[i + 1][0] =
            ((dp[i][0] * (h - 1)) % mod + dp[i][1] - dp[i][2] + dp[i][3]) % mod;
        dp[i + 1][1] =
            ((dp[i][1] * (w - 1)) % mod + dp[i][0] - dp[i][2] + dp[i][3]) % mod;
        dp[i + 1][2] = (dp[i][0] + dp[i][1] - 2 * dp[i][2]) % mod;
        dp[i + 1][3] = ((dp[i][0] - dp[i][2]) * (w - 1) % mod +
                        (dp[i][1] - dp[i][2]) * (h - 1) % mod +
                        dp[i][3] * (h - 2 + w - 2) % mod) %
                       mod;
        rep(j, 4) dp[i + 1][j] %= mod;
    }

    cout << dp[h][2] << "\n";
    return 0;
}