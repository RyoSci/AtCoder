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
    Int d, g;
    cin >> d >> g;
    g /= 100;
    vector<Int> p(d), c(d);
    rep(i, d) {
        Int pi, ci;
        cin >> pi >> ci;
        p[i] = pi, c[i] = ci / 100;
    }
    vector<vector<Int>> dp(d + 1, vector<Int>(g + 1, INF));
    //    dp[i][j]<-i*100点までの問題を見て、j点にするテストの問題数の最小値
    dp[0][0] = 0;
    rep(i, d) {
        rep(j, g + 1) {
            if (dp[i][j] == INF) continue;
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j]);
            rep_s(k, 1, p[i] + 1) {
                dp[i + 1][min(g, j + (i + 1) * k)] =
                    min(dp[i + 1][min(g, j + (i + 1) * k)], dp[i][j] + k);
            }
            dp[i + 1][min(g, j + (i + 1) * p[i] + c[i])] = min(
                dp[i + 1][min(g, j + (i + 1) * p[i] + c[i])], dp[i][j] + p[i]);
        }
    }
    cout << dp[d][g] << "\n";
    // rep(i, d + 1) {
    //     for (Int a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }

    return 0;
}