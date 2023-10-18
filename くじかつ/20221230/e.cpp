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
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector dp(2, vector(n + 1, vector(2, INF)));
    dp[0][1][0] = 0;
    rep_s(i, 1, n) {
        chmin(dp[0][i + 1][1], dp[0][i][0] + a[i]);
        chmin(dp[0][i + 1][1], dp[0][i][1] + a[i]);
        chmin(dp[0][i + 1][0], dp[0][i][1]);
    }

    dp[1][1][1] = a[0];
    rep_s(i, 1, n) {
        chmin(dp[1][i + 1][1], dp[1][i][0] + a[i]);
        chmin(dp[1][i + 1][1], dp[1][i][1] + a[i]);
        chmin(dp[1][i + 1][0], dp[1][i][1]);
    }

    ll ans = min(min(dp[0][n][1], dp[1][n][0]), dp[1][n][1]);
    cout << ans << "\n";

    return 0;
}