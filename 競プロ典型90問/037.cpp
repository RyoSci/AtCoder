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

void chmax(Int &x, Int y) {
    if (x < y) x = y;
}

int main() {
    // Int w, n;
    // cin >> w >> n;
    Int w = 10000;
    Int n = 500;
    vector<Int> l(n);
    vector<Int> r(n);
    vector<Int> v(n);
    // rep(i, n) { cin >> l[i] >> r[i] >> v[i]; }
    rep(i, n) {
        l[i] = 1;
        r[i] = w;
        v[i] = 1000000000;
    }

    vector<vector<Int>> dp(n + 1, vector<Int>(w + 1, -INF));
    dp[0][0] = 0;
    rep(i, n) {
        rep(j, w + 1) {
            if (dp[i][j] == -INF) continue;
            // 使う場合
            rep_s(k, l[i], r[i] + 1) {
                if (j + k <= w) {
                    chmax(dp[i + 1][min(w, j + k)], dp[i][j] + v[i]);
                }
            }
            // 使わない場合
            chmax(dp[i + 1][j], dp[i][j]);
        }
    }
    if (dp[n][w] == -INF)
        cout << -1 << "\n";
    else
        cout << dp[n][w] << "\n";

    return 0;
}