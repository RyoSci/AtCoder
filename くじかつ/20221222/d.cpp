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
using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
// #define MOD 998244353
#define INF (1LL << 60)
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
    ll n, k;
    cin >> n >> k;
    vector dp(3000, vector(3000, mint(0)));
    dp[0][0] = 1;
    rep(i, 3000 - 1) rep(j, 3000 - 1) {
        dp[i + 1][j] += dp[i][j];
        dp[i + 1][j + 1] += dp[i][j];
    }
    auto conbi = [&](ll n, ll k) {
        if (n < k | k < 0) return mint(0);
        return dp[n][k];
    };

    rep_s(i, 0, k) {
        mint ans = 1;
        ll r = n - k, b = k;
        if (i > 0) b -= i + 1;
        r -= i;
        ans *= conbi(i + b, b);
        ans *= conbi(i + 1 + r, r);
        cout << ans.val() << "\n";
    }
    // cout << dp[3][2].val() << "\n";
    return 0;
}