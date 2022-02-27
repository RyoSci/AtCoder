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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> dp(10, vector<ll>(10));
    rep(i, 10) {
        rep(j, 10) { cin >> dp[i][j]; }
    }

    rep(k, 10) {
        rep(i, 10) {
            rep(j, 10) { chmin(dp[i][j], dp[i][k] + dp[k][j]); }
        }
    }

    ll ans = 0;
    rep(i, h) {
        rep(j, w) {
            ll aij;
            cin >> aij;
            if (aij == -1) continue;
            ans += dp[aij][1];
        }
    }

    cout << ans << "\n";

    return 0;
}