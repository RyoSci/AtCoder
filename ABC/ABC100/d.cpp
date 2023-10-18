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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> x(n), y(n), z(n);
    rep(i, n) cin >> x[i] >> y[i] >> z[i];

    vector<vector<T>> dp(n + 1,
                         vector<T>(1 << 3, make_tuple(-INF, -INF, -INF)));

    // vector<vector<vector<T>>> dp(
    //     n + 1,
    //     vector<vector<T>>(m + 1, vector<T>(1 << 3, make_tuple(0, 0, 0))));

    // dp[i][j][k]:=i番目の中からj個選んでk(000-111)への寄与が最大となるtupple
    rep(k, 1 << 3) dp[0][k] = make_tuple(0, 0, 0);
    // rep(k, 1 << 3) dp[0][0][k] = make_tuple(0, 0, 0);

    // rep(i, n) rep(j, m) rep(k, 1 << 3) {
    rep(i, n) rep_r(j, m - 1, -1) rep(k, 1 << 3) {
        // auto [xi, yi, zi] = dp[i][j][k];
        auto [xi, yi, zi] = dp[j][k];
        ll nxi = xi, nyi = yi, nzi = zi;
        if ((k >> 0) & 1)
            nxi += x[i];
        else
            nxi -= x[i];
        if ((k >> 1) & 1)
            nyi += y[i];
        else
            nyi -= y[i];
        if ((k >> 2) & 1)
            nzi += z[i];
        else
            nzi -= z[i];

        // auto [xi2, yi2, zi2] = dp[i + 1][j + 1][k];
        auto [xi2, yi2, zi2] = dp[j + 1][k];
        if (nxi + nyi + nzi > xi2 + yi2 + zi2)
            dp[j + 1][k] = make_tuple(nxi, nyi, nzi);
        // dp[i + 1][j + 1][k] = make_tuple(nxi, nyi, nzi);
        // auto [xi3, yi3, zi3] = dp[i + 1][j][k];
        // if (xi + yi + zi > xi3 + yi3 + zi3)
        //     dp[i + 1][j][k] = make_tuple(xi, yi, zi);
    }

    ll ans = 0;
    rep(i, 1 << 3) {
        auto [xi, yi, zi] = dp[m][i];
        // auto [xi, yi, zi] = dp[n][m][i];
        ans = max(ans, xi + yi + zi);
    }

    cout << ans << "\n";
    return 0;
}