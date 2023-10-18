// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
using namespace atcoder;
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<int, int> P;
typedef tuple<int, int, int> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    int h, w;
    cin >> h >> w;
    vector a(h, vector(w, 0));
    // rep(i, h) rep(j, w) a[i][j] = 80 - i;
    rep(i, h) rep(j, w) cin >> a[i][j];
    vector b(h, vector(w, 0));
    // rep(i, h) rep(j, w) b[i][j] = i;
    rep(i, h) rep(j, w) cin >> b[i][j];

    int top = 160 * 160;
    vector dp(h, vector(w, vector(top + 1, 0)));

    int nk;
    nk = top / 2 + a[0][0] - b[0][0];
    dp[0][0][nk] = 1;
    nk = top / 2 - a[0][0] + b[0][0];
    dp[0][0][nk] = 1;

    rep(i, h) rep(j, w) {
        rep(k, top + 1) {
            if (dp[i][j][k] == 0) continue;
            int nk;
            // 下
            if (i < h - 1) {
                nk = k;
                nk += a[i + 1][j] - b[i + 1][j];
                if (0 <= nk and nk <= top) dp[i + 1][j][nk] = 1;
            }
            // 右
            if (j < w - 1) {
                nk = k;
                nk += -a[i][j + 1] + b[i][j + 1];
                if (0 <= nk and nk <= top) dp[i][j + 1][nk] = 1;
            }
        }
    }

    int ans = top;
    rep(k, top + 1) {
        if (dp[h - 1][w - 1][k]) ans = min(ans, abs(k - top / 2));
    }
    cout << ans << "\n";
    return 0;
}