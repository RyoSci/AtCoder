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
    string s;
    cin >> s;
    ll n = s.length();
    string c = "chokudai";
    ll m = c.length();

    vector<vector<ll>> dp(m + 1, vector<ll>(n + 1, 0));

    // dp[i][j]<-cをi文字目までつなげた時の、sをj文字目までみた時の作れる数
    rep_s(i, 1, n + 1) {
        if (s[i - 1] == 'c') dp[1][i] += 1;
        dp[1][i] += dp[1][i - 1];
    }

    rep_s(i, 2, m + 1) {
        rep_s(j, 1, n + 1) {
            dp[i][j] += dp[i][j - 1];
            if (c[i - 1] == s[j - 1]) dp[i][j] += dp[i - 1][j - 1];
            dp[i][j] %= MOD;
        }
    }
    cout << dp[m][n] << "\n";
    return 0;
}