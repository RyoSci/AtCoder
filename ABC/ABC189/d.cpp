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
    ll n;
    cin >> n;
    vector<string> s(n);
    rep(i, n) cin >> s[i];
    vector<vector<ll>> dp(n + 1, vector<ll>(2, 0));

    dp[0][0] = 1;
    dp[0][1] = 1;
    rep(i, n) {
        if (s[i] == "AND") {
            dp[i + 1][1] += dp[i][1];
            dp[i + 1][0] += dp[i][1] + 2 * dp[i][0];
        } else {
            dp[i + 1][1] += 2 * dp[i][1] + dp[i][0];
            dp[i + 1][0] += dp[i][0];
        }
    }

    cout << dp[n][1] << "\n";
    return 0;
}