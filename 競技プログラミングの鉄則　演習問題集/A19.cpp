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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n, W;
    cin >> n >> W;
    vector<ll> w(n, 0), v(n, 0);
    rep(i, n) cin >> w[i] >> v[i];

    vector dp(n + 1, vector(W + 1, -1ll));
    dp[0][0] = 0;
    rep(i, n) {
        rep(j, W + 1) {
            if (dp[i][j] == -1) continue;
            chmax(dp[i + 1][j], dp[i][j]);
            if (j + w[i] <= W) chmax(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
        }
    }

    ll ans = 0;
    rep(i, W + 1) chmax(ans, dp[n][i]);

    cout << ans << "\n";

    return 0;
}