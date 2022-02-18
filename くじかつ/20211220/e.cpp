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

void chmin(Int &x, Int y) {
    x = min(x, y);
    return;
}

int main() {
    Int n;
    cin >> n;
    Int n2 = 1 << n;
    vector<vector<Int>> dis(n, vector<Int>(n));
    vector<Int> x(n), y(n), z(n);
    rep(i, n) { cin >> x[i] >> y[i] >> z[i]; }

    rep(i, n) {
        rep(j, n) dis[i][j] =
            abs(x[j] - x[i]) + abs(y[j] - y[i]) + max(0, z[j] - z[i]);
    }

    vector<vector<Int>> dp(n2, vector<Int>(n, INF));
    rep(i, n) {
        if (i == 0) continue;
        chmin(dp[1 << i][i], dis[0][i]);
    }

    rep(i, n2) {
        rep(j, n) {
            if (!(i >> j & 1)) continue;
            rep(k, n) { chmin(dp[i | 1 << k][k], dp[i][j] + dis[j][k]); }
        }
    }

    cout << dp[n2 - 1][0] << "\n";
    // rep(i, n2) {
    //     for (Int a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }
    return 0;
}