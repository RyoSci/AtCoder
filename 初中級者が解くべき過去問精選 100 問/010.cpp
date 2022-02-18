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
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++) cin >> a[i];
    vector<vector<Int>> dp(n + 1, vector<Int>(2001));
    dp[0][0] = 1;
    rep(i, n) {
        rep(j, 2001) {
            if (dp[i][j] == 0) continue;
            dp[i + 1][j] = dp[i][j];
            if (j + a[i] <= 2000) dp[i + 1][j + a[i]] = dp[i][j];
        }
    }

    Int q;
    cin >> q;
    vector<Int> m(q);
    for (Int i = 0; i < q; i++) cin >> m[i];

    rep(i, q) {
        if (dp[n][m[i]] == 1)
            cout << "yes"
                 << "\n";
        else
            cout << "no"
                 << "\n";
    }
    return 0;
}