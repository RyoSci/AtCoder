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
    Int n, m;
    cin >> n >> m;
    vector<Int> a(m);
    for (Int i = 0; i < m; i++) cin >> a[i];
    vector<Int> dp(n + 1);
    dp[0] = 1;
    rep(i, m) { dp[a[i]] = -1; }
    rep(i, n) {
        if (dp[i] == -1) continue;
        if (dp[i + 1] != -1) {
            dp[i + 1] += dp[i];
            dp[i + 1] %= MOD;
        }

        if (i + 2 <= n) {
            if (dp[i + 2] != -1) {
                dp[i + 2] += dp[i];
                dp[i + 2] %= MOD;
            }
        }
    }

    cout << dp[n] << "\n";
    return 0;
}