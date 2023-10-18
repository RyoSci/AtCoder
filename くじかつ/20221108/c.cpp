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
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, m, k;
    cin >> n >> m >> k;
    vector<vector<mint>> dp(n + 1, vector<mint>(k + 1, 0));
    dp[0][0] = 1;

    rep(i, n) {
        rep(j, k) {
            if (dp[i][j] == 0) continue;
            rep_s(l, 1, m + 1) {
                if (j + l <= k) dp[i + 1][j + l] += dp[i][j];
            }
        }
    }

    mint ans = 0;
    rep(i, k + 1) ans += dp[n][i];
    cout << ans.val() << "\n";
    return 0;
}